"""
This file retrieves job postings from the EURES job portal 
"""

import requests
import pandas as pd
import time
import math
import re
from bs4 import BeautifulSoup
from nuts import COUNTRY_CODE_TO_NAME, NUTS_REGIONS
from scraping.config import (MODE,
                    EURES_URL,
                    EURES_HEADERS,
                    COUNTRY_CODES,
                    EELISA_COUNTRIES,
                    JOBS_PER_EELISA_COUNTRY,
                    RESULTS_PER_PAGE,
                    JOBS_PER_NON_EELISA_COUNTRY,
                    REQUEST_DELAY,
                    OUTPUT_CSV,
                    SEARCH_KEYWORDS)
from scraping.scraping_logic import (
    clean_html,
    classify_domain,
    extract_company_from_text,
    infer_country_from_location_map,
    extract_region_from_location_map
)

# -----------------------------
# CONFIGS
# -----------------------------
if MODE == "test":
    print("\n=== RUNNING IN TEST MODE ===\n")
    SELECTED_COUNTRIES = ["cz"]     
    SELECTED_KEYWORDS = ["engineer"]
else:
    print("\n=== RUNNING FULL SCRAPER ===\n")
    SELECTED_COUNTRIES = COUNTRY_CODES
    SELECTED_KEYWORDS = SEARCH_KEYWORDS


# -----------------------------
# CORE SCRAPING LOGIC
# -----------------------------
def fetch_page(country_code: str | None,
               keyword: str,
               page: int,
               results_per_page: int = RESULTS_PER_PAGE) -> dict | None:
    """
    Fetch one page of results for a given country & keyword.
    """
    payload = {
        "resultsPerPage": results_per_page,
        "page": page,
        "sortSearch": "BEST_MATCH",
        "keywords": [
            {
                "keyword": keyword,
                "specificSearchCode": "EVERYWHERE"
            }
        ],
        "locationCodes": [country_code] if country_code else [],
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
        "skillUris": []
    }

    r = requests.post(EURES_URL, json=payload, headers=EURES_HEADERS, timeout=20)
    print(f"[{country_code or 'ALL'} | {keyword} | page {page}] Status: {r.status_code}")

    if r.status_code != 200:
        print("  -> Error response (first 300 chars):", r.text[:300])
        return None

    try:
        return r.json()
    except Exception as e:
        print("  -> JSON decode error:", e)
        print(r.text[:300])
        return None


def fetch_jobs_for_country(country_code: str,
                           max_jobs: int = JOBS_PER_NON_EELISA_COUNTRY) -> list[dict]:
    """
    Fetch up to max_jobs for a given country, distributing jobs across all SELECTED_KEYWORDS.
    """
    from scraping.config import JOBS_PER_KEYWORD_EELISA, JOBS_PER_KEYWORD_NON_EELISA

    all_jobs = []
    seen_ids = set()
    if country_code in EELISA_COUNTRIES:
        jobs_per_keyword = JOBS_PER_KEYWORD_EELISA
    else:
        jobs_per_keyword = JOBS_PER_KEYWORD_NON_EELISA

    for kw in SELECTED_KEYWORDS:
        page = 1
        kw_jobs = 0
        while kw_jobs < jobs_per_keyword and len(all_jobs) < max_jobs:
            data = fetch_page(country_code, kw, page, RESULTS_PER_PAGE)
            time.sleep(REQUEST_DELAY)

            if not data:
                break

            jvs = data.get("jvs", [])
            if not jvs:
                break

            for job in jvs:
                job_id = job.get("id")
                if job_id in seen_ids:
                    continue
                seen_ids.add(job_id)

                raw_desc = job.get("description", "")
                clean_desc = clean_html(raw_desc)
                title = job.get("title", "")

                country_name = infer_country_from_location_map(job.get("locationMap"))
                domain = classify_domain(title, clean_desc)

                employer = job.get("employer")
                company_name = employer.get("name") if isinstance(employer, dict) else None

                if not company_name:
                    extracted = extract_company_from_text(clean_desc)
                    if extracted:
                        company_name = extracted

                all_jobs.append({
                    "job_id": job_id,
                    "job_title": title,
                    "date": job.get("dateOfPublication") or job.get("creationDate"),
                    "company_name": company_name,
                    "country": country_name,
                    "country_code": country_code.upper(),
                    "region": extract_region_from_location_map(job.get("locationMap")),
                    "field": domain,
                    "full_description": clean_desc,
                })

                kw_jobs += 1
                if kw_jobs >= jobs_per_keyword or len(all_jobs) >= max_jobs:
                    break

            if len(jvs) < RESULTS_PER_PAGE:
                break

            page += 1

    return all_jobs



# -----------------------------
# MAIN
# -----------------------------
def save_results(existing_df, all_rows):
    """
    Saves current CSV when scraping interrupted mid run 
    """
    df = pd.concat([existing_df, pd.DataFrame(all_rows)], ignore_index=True)
    df.drop_duplicates(subset="job_id", inplace=True)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"Saved dataset to {OUTPUT_CSV} (unique jobs: {len(df)})")


if __name__ == "__main__":
    all_rows = []
    try:
        existing_df = pd.read_csv(OUTPUT_CSV)
        existing_ids = set(existing_df["job_id"])
    except (FileNotFoundError, pd.errors.EmptyDataError):
        existing_df = pd.DataFrame()
        existing_ids = set()

    try:
        for code in SELECTED_COUNTRIES:
            print(f"\n========== Scraping country: {code.upper()} ==========")
            if code in EELISA_COUNTRIES:
                max_jobs = JOBS_PER_EELISA_COUNTRY
            else:
                max_jobs = JOBS_PER_NON_EELISA_COUNTRY
            jobs = fetch_jobs_for_country(code, max_jobs=max_jobs)
            # Only add jobs not already in the CSV
            new_jobs = [job for job in jobs if job["job_id"] not in existing_ids]
            print(f"  -> Collected {len(new_jobs)} new jobs for {code.upper()}")
            all_rows.extend(new_jobs)
            existing_ids.update(job["job_id"] for job in new_jobs)

        print(f"\nTotal new jobs collected: {len(all_rows)}")
        save_results(existing_df, all_rows)
    except KeyboardInterrupt:
        print("\nInterrupted by user. Saving progress...")
        save_results(existing_df, all_rows)