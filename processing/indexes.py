import pandas as pd

jobs_dataset = 'input_path'
df = pd.read_csv(jobs_dataset)

# --------------------
# Formalizing the job_id to FR1, FR2... unifomred type for primary inde
# --------------------

df['job_id'] = (df.groupby('country_code').cumcount() + 1).astype(str)
df['job_id'] = df['country_code'].str.upper()+df['job_id']

df.to_csv(jobs_dataset, index=False)