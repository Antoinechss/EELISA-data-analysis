<p align="center">
  <img src="https://github.com/user-attachments/assets/026a3c60-1574-4e4b-bce3-ff71f72786c6" alt="EELISA – European Engineering Learning Innovation & Science Alliance" width="360"/>
</p>

<h1 align="center">European Job Postings Dataset for Transition Engineering</h1>

<p align="center">
  <em>
    A curated dataset of job postings designed to support the construction of a European competence framework for transition engineers.
  </em>
</p>

---

## 1. Project Context

This repository hosts a structured dataset of **job postings related to engineering, sustainability, and socio-technical transitions**, collected within the framework of the **EELISA Data Science Mission**.

The primary objective of this dataset is to support the **identification, analysis, and structuring of competencies required for transition engineers in Europe**, based on real labor market demand.

---

## 2. Dataset Purpose

The dataset is intended to enable:

- Identification of **core and emerging competencies** for transition engineers  
- Analysis of **skills, tools, and knowledge areas** required across European job markets  
- Contribution to the design of a **competence framework** aligned with societal, environmental, and technological transitions  
- Support for educational program design and policy-oriented research  

This dataset is not intended for commercial use.

---

## 3. Data Collection Pipeline

The dataset was built through a multi-stage pipeline:

1. **Web Scraping**  
   - Automated extraction of publicly available job postings from online employment platforms  
   - Focus on roles related to engineering, sustainability, energy transition, digital transformation, and systems thinking  

2. **Data Cleaning and Normalization**  
   - Removal of duplicates and incomplete entries  
   - Standardization of job titles, locations, and contract information  
   - Text preprocessing for descriptions and skill sections  

3. **Structuring and Enrichment**  
   - Organization into tabular format suitable for analysis  
   - Preparation for downstream NLP tasks (skill extraction, clustering, taxonomy building)  

A complete description of sources, variables, preprocessing steps, and limitations is provided in the **dataset note**.

---

## 4. Technical Stack

The dataset pipeline relies on the following technologies:

- **Python**  
- **BeautifulSoup / Requests** for web scraping  
- **Pandas** and **NumPy** for data processing  
- **Regular Expressions** and text preprocessing utilities  
- **Jupyter Notebooks** for exploration and validation  

The dataset is provided in a **CSV format** to ensure compatibility with a wide range of analytical tools.

---
## 5. Repository Structure

```text
.
├── datasets/
│   ├── raw/
│   └── processed/
├── scraping/
│   ├── __pycache__/
│   ├── config.py
│   ├── eures_scrape.py
│   ├── turkey_scrape.py
│   ├── scraping_logic.py
│   └── nuts.py
├── processing/
│   ├── __pycache__/
│   ├── coordinates.py
│   ├── dates.py
│   ├── deduplicate.py
│   ├── enrich_field.py
│   ├── indexes.py
│   ├── TR_processing.py
│   ├── inferred_fields.json
│   └── translation/
│       └── translation_pipeline.py
├── __pycache__/
├── venv/
└── README.md
```

---

## 6. Methodological Reference

All methodological choices, including:

- selection criteria  
- variable definitions  
- ethical considerations  
- biases and limitations  

are documented in the **dataset note**, which should be consulted prior to any analytical use.

---

## 7. Disclaimer and Ethics

This dataset is composed exclusively of **publicly available information**.  
It is intended solely for **academic, educational, and research purposes**.

Users are responsible for ensuring compliance with applicable legal and ethical standards when using the data.

---

## 8. Acknowledgements

This work was developed within the **EELISA – European Engineering Learning Innovation & Science Alliance**,  
as part of a **Data Science Mission** dedicated to engineering education and societal transition challenges.

