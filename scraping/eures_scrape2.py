"""
Completing the dataset with additional job offers from sparse countries 
"""

import requests
import pandas as pd
import time
import re
from bs4 import BeautifulSoup

from nuts import COUNTRY_CODE_TO_NAME, NUTS_REGIONS
from scraping.config import (
    EURES_URL,
    EURES_HEADERS,
    RESULTS_PER_PAGE,
    REQUEST_DELAY,
    SEARCH_KEYWORDS,
    JOBS_PER_KEYWORD_EELISA,
    JOBS_PER_KEYWORD_NON_EELISA,
    JOBS_PER_EELISA_COUNTRY,
    JOBS_PER_NON_EELISA_COUNTRY,
    EELISA_COUNTRIES,
    DOMAIN_PATTERNS,
)

# ======================================================
# OUTPUT (NEW DATASET)
# ======================================================
OUTPUT_CSV = "eures_additional_target_countries.csv"


# ======================================================
# ONLY COUNTRIES TO SCRAPE
# ======================================================
TARGET_COUNTRIES = [
    "bg", "hr", "cy", "ee",
    "gr", "hu", "lv", "lt",
    "pl", "pt", "ro", "es"
]


# ======================================================
# PRIORITY BOOST
# ======================================================
PRIORITY_COUNTRIES = {
    # EELISA focus
    "hu": 3,
    "es": 3,
    "ro": 3,

    # Others
    "bg": 2,
    "hr": 2,
    "cy": 2,
    "ee": 2,
    "gr": 2,
    "lv": 2,
    "lt": 2,
    "pl": 2,
    "pt": 2,
}


# ======================================================
# TEXT & DOMAIN LOGIC (UNCHANGED)
# ======================================================
def clean_html(html_text):
    if not html_text:
        return ""
    soup = BeautifulSoup(html_text, "html.parser")
    return soup.get_text(" ", strip=True)


def classify_domain(title, description):
    text = (title or "").lower() + " " + (description or "").lower()
    for domain, patterns in DOMAIN_PATTERNS:
        if any(p in text for p in patterns):
            return domain
    return "Other / Undefined"



def extract_company_from_text(text):
    if not text:
        return None

    patterns = [
        r"for\s+([A-Z][A-Za-z0-9&\-\s']+)",
        r"at\s+([A-Z][A-Za-z0-9&\-\s']+)",
        r"join\s+([A-Z][A-Za-z0-9&\-\s']+)",
        r"with\s+([A-Z][A-Za-z0-9&\-\s']+)",
        r"chez\s+([A-Z][A-Za-z0-9&\-\s']+)",
        r"pour\s+([A-Z][A-Za-z0-9&\-\s']+)",
    ]

    for p in patterns:
        m = re.search(p, text, flags=re.IGNORECASE)
        if m:
            name = re.sub(r"[.,;:]+$", "", m.group(1).strip())
            if len(name.split()) <= 6:
                return name
    return None


def infer_country_from_location_map(location_map):
    if not location_map:
        return None
    try:
        code = next(iter(location_map.keys()))
        return COUNTRY_CODE_TO_NAME.get(code.lower(), code.upper())
    except Exception:
        return None


def extract_region_from_location_map(location_map):
    if not location_map:
        return None
    try:
        country_code = next(iter(location_map.keys()))
        nuts = location_map[country_code]
        if not nuts:
            return None
        return NUTS_REGIONS.get(nuts[0][:3], nuts[0][:3])
    except Exception:
        return None


# ======================================================
# EURES FETCH
# ======================================================
def fetch_page(country_code, keyword, page):
    payload = {
        "resultsPerPage": RESULTS_PER_PAGE,
        "page": page,
        "sortSearch": "BEST_MATCH",
        "keywords": [{"keyword": keyword, "specificSearchCode": "EVERYWHERE"}],
        "locationCodes": [country_code],
        "educationAndQualificationLevelCodes": [],
        "euresFlagCodes": [],
        "occupationUris": [],
        "otherBenefitsCodes": [],
        "positionOfferingCodes": [],
        "positionScheduleCodes": [],
        "publicationPeriod": None,
        "requiredExperienceCodes": [],
        "requiredLanguages": [],
        "sectorCodes": [],
        "skillUris": [],
    }

    r = requests.post(EURES_URL, json=payload, headers=EURES_HEADERS, timeout=20)
    print(f"[{country_code.upper()} | {keyword} | page {page}] → {r.status_code}")

    if r.status_code != 200:
        return None

    return r.json()


# ======================================================
# CORE SCRAPER (TARGET COUNTRIES ONLY)
# ======================================================
def fetch_jobs_for_country(country_code):
    all_jobs = []
    seen_ids = set()

    if country_code in EELISA_COUNTRIES:
        base_kw = JOBS_PER_KEYWORD_EELISA
        base_max = JOBS_PER_EELISA_COUNTRY
    else:
        base_kw = JOBS_PER_KEYWORD_NON_EELISA
        base_max = JOBS_PER_NON_EELISA_COUNTRY

    multiplier = PRIORITY_COUNTRIES.get(country_code, 1)
    jobs_per_keyword = base_kw * multiplier
    max_jobs = base_max * multiplier

    for kw in SEARCH_KEYWORDS:
        page = 1
        kw_count = 0

        while kw_count < jobs_per_keyword and len(all_jobs) < max_jobs:
            data = fetch_page(country_code, kw, page)
            time.sleep(REQUEST_DELAY)

            if not data or not data.get("jvs"):
                break

            for job in data["jvs"]:
                job_id = job.get("id")
                if job_id in seen_ids:
                    continue

                seen_ids.add(job_id)

                desc = clean_html(job.get("description"))
                title = job.get("title")

                employer = job.get("employer") or {}
                company = employer.get("name") or extract_company_from_text(desc)

                all_jobs.append({
                    "job_id": job_id,
                    "job_title": title,
                    "date": job.get("dateOfPublication") or job.get("creationDate"),
                    "company_name": company,
                    "country": infer_country_from_location_map(job.get("locationMap")),
                    "country_code": country_code.upper(),
                    "region": extract_region_from_location_map(job.get("locationMap")),
                    "field": classify_domain(title, desc),
                    "full_description": desc,
                })

                kw_count += 1
                if kw_count >= jobs_per_keyword or len(all_jobs) >= max_jobs:
                    break

            page += 1

    return all_jobs

def save_progress(rows, output_csv):
    df = pd.DataFrame(rows)
    df.drop_duplicates(subset="job_id", inplace=True)
    df.to_csv(output_csv, index=False)
    print(f"💾 Progress saved: {len(df)} jobs")


# ======================================================
# MAIN
# ======================================================
if __name__ == "__main__":

    try:
        existing_df = pd.read_csv(OUTPUT_CSV)
        existing_ids = set(existing_df["job_id"])
        all_rows = existing_df.to_dict("records")
        print(f"🔁 Resuming from existing file ({len(existing_ids)} jobs loaded)")
    except FileNotFoundError:
        all_rows = []
        existing_ids = set()
        print("🆕 Starting fresh scrape")

    try:
        for code in TARGET_COUNTRIES:
            print(f"\n========== Scraping {code.upper()} ==========")

            rows = fetch_jobs_for_country(code)

            # keep only truly new jobs
            new_rows = [r for r in rows if r["job_id"] not in existing_ids]

            print(f"Collected {len(new_rows)} NEW jobs")

            all_rows.extend(new_rows)
            existing_ids.update(r["job_id"] for r in new_rows)

            # SAVE AFTER EACH COUNTRY ✅
            save_progress(all_rows, OUTPUT_CSV)

    except KeyboardInterrupt:
        print("\n⛔ Interrupted by user — saving progress...")
        save_progress(all_rows, OUTPUT_CSV)
