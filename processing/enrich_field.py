import pandas as pd
from scraping.config import FIELD_KEYWORDS
from rapidfuzz import fuzz

jobs_dataset = "Path"
df = pd.read_csv(jobs_dataset)

## TODO

df.to_csv('/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/datasets/european_jobs_enriched_fields.csv', index=False)