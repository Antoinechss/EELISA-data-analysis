import pandas as pd

main_path = '/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/european_jobs_dataset.csv'
turkey_path = '/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/turkey_jobs_dataset.csv'
output_path = '/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/european_jobs_dataset_full.csv'

# Load datasets
df_main = pd.read_csv(main_path)
df_tr = pd.read_csv(turkey_path)

# Ensure column order matches
df_tr = df_tr[df_main.columns]

# Combine
df = pd.concat([df_main, df_tr], ignore_index=True)

# Recreate job_id consistently
df['job_id'] = df.groupby('country_code').cumcount() + 1
df['job_id'] = df['country_code'].str.upper() + df['job_id'].astype(str)

# Save
df.to_csv(output_path, index=False)
