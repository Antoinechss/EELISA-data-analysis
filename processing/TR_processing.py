import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import re
import os

HEADERS = {"User-Agent": "Mozilla/5.0"}

INPUT_CSV = "/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/turkey_yenibiris_all_keywords.csv"
PARTIAL_CSV = "turkey_yenibiris_EURES_partial.csv"
OUTPUT_CSV = "turkey_yenibiris_EURES_format.csv"


def extract_description_and_date(url):
    """Scrape full description + Güncelleme Tarihi."""
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        # --- Description block ---
        desc_el = (
            soup.select_one("div.well.mb0.mainInfos")
            or soup.select_one("div.mainInfos")
            or soup.select_one("div.detailInfos")
            or soup.select_one("div.col-lg-8.col-md-8.leftColumnForLarge div.well")
        )
        full_desc = desc_el.get_text(" ", strip=True) if desc_el else ""

        # --- Date extraction ---
        posted_date = None
        for li in soup.select("div.additionalInfos ul li"):
            label = li.select_one("label")
            span = li.select_one("span")
            if label and span and "Güncelleme" in label.get_text(strip=True):
                posted_date = span.get_text(strip=True)

        return full_desc, posted_date

    except Exception as e:
        print(f"❌ Error on {url}: {e}")
        return "", None


def extract_job_id(url):
    m = re.search(r"/(\d+)$", url)
    return m.group(1) if m else None



# ============================================================
#                     LOAD OR RESUME
# ============================================================

if os.path.exists(PARTIAL_CSV):
    print("🔄 Resume mode enabled — loading partial progress…")
    partial_df = pd.read_csv(PARTIAL_CSV)
    df = pd.read_csv(INPUT_CSV)

    # Merge partial progress into main df
    df["full_description"] = partial_df.get("full_description")
    df["date"] = partial_df.get("date")

else:
    print("➡️ Starting fresh — no partial file found.")
    df = pd.read_csv(INPUT_CSV)
    df["full_description"] = None
    df["date"] = None



# ============================================================
#                     SCRAPING LOOP
# ============================================================

total = len(df)
print(f"\nScraping full descriptions + dates for {total} jobs…\n")

try:
    for i, row in df.iterrows():
        url = row["url"]

        # ⚠️ SKIP already scraped
        if isinstance(row["full_description"], str) and len(row["full_description"].strip()) > 5:
            print(f"[{i+1}/{total}] SKIP — already scraped")
            continue

        print(f"[{i+1}/{total}] {url}")

        full_desc, posted_date = extract_description_and_date(url)

        df.at[i, "full_description"] = full_desc
        df.at[i, "date"] = posted_date

        # Save partial progress
        df[["url", "full_description", "date"]].to_csv(PARTIAL_CSV, index=False)

        time.sleep(0.3)

except KeyboardInterrupt:
    print("\n\n⚠️ Interrupted by user — saving progress...")
    df[["url", "full_description", "date"]].to_csv(PARTIAL_CSV, index=False)
    print(f"✔ Partial data saved to {PARTIAL_CSV}")
    exit(0)



# ============================================================
#                     FINISH + FORMAT EURES
# ============================================================

print("\n✔ All descriptions scraped successfully!")

df["job_id"] = df["url"].apply(extract_job_id)
df["job_title"] = df["title"]
df["company_name"] = df["company"]
df["country"] = "Turkey"
df["country_code"] = "TR"
df["region"] = df["location"].apply(lambda x: x.split(",")[0].strip() if isinstance(x, str) else None)
df["field"] = "Other/Undefined"

final_df = df[[
    "job_id",
    "job_title",
    "date",
    "company_name",
    "country",
    "country_code",
    "region",
    "field",
    "full_description"
]]

final_df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8")

# Remove partial file now that scraping is complete
if os.path.exists(PARTIAL_CSV):
    os.remove(PARTIAL_CSV)

print("🎉 DONE — saved final dataset to:", OUTPUT_CSV)
print("Final shape:", final_df.shape)
