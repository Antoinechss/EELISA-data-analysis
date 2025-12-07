# EELISA Job Market Data Scraping Pipeline

This project builds a complete data pipeline for collecting, cleaning, translating, and enriching job postings for the EELISA Data Science Mission.
It integrates job vacancies from:

* EURES (European Commission job mobility portal)

* Yenibiris (Turkey’s leading job platform)

and outputs a unified, analysis-ready dataset.

📂 Project Structure
datasets/               # Raw and processed datasets
processing/
│── translation/        # Translation scripts & utilities
│── dates.py            # Date parsing & normalization
│── coordinates.py      # Geocoding utilities
│── deduplicate.py      # Duplicate removal
│── enrich_field.py     # AI-based job field classification
│── indexes.py          # Index cleanup
│── inferred_fields.json# Cache for classification
│── TR_processing.py    # Turkey-specific preprocessing
scraping/
│── config.py           # Scraper settings and endpoints
│── eures_scraper.py    # Scrapes EURES platform
│── turkey_scraper.py   # Scrapes Yenibiris
│── scraping_utils.py   # Shared scraping helpers

Pipeline Overview

Scraping

* python scraping/eures_scraper.py
* python scraping/turkey_scraper.py


Cleaning & Preprocessing

* python processing/deduplicate.py
* python processing/dates.py
* python processing/coordinates.py


Translation 

* python processing/translation/translate.py


Job Field Classification

* python processing/enrich_field.py

License : Research use — part of the EELISA Data Science Mission.