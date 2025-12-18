import pandas as pd

path = '/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/scraping/dataset_filtered.csv'
df = pd.read_csv(path)

# --------------------
# Formalizing the job_id to FR1, FR2... unifomred type for primary inde
# --------------------

df['job_id'] = (df.groupby('country_code').cumcount() + 1).astype(str)
df['job_id'] = df['country_code'].str.upper()+df['job_id']

df.to_csv(path, index=False)