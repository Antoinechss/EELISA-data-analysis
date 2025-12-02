import pandas as pd
from scraping.config import FIELD_KEYWORDS

jobs_dataset = '/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/datasets/european_jobs.csv'
df = pd.read_csv(jobs_dataset)

### INFER FIELD FROM TITLE AND DESCRIPTION ###

df.to_csv('/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/datasets/european_jobs_enriched_fields.csv', index=False)


