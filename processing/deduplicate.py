import pandas as pd
from rapidfuzz import fuzz

jobs_dataset = 'input_path'
df = pd.read_csv(jobs_dataset)

# ------------------------
# Removing duplicate job offers using fuzzy matching 
# ------------------------
df = df.drop_duplicates(subset=["job_title", "company_name", "full_description"])

df["block"] = df["job_title"].str[:10] + df["company_name"].str[:10]  

to_drop = set()
for block_val, block_df in df.groupby("block"):
    idxs = block_df.index.tolist()
    for i, idx_i in enumerate(idxs):
        if idx_i in to_drop:
            continue
        for idx_j in idxs[i+1:]:
            if idx_j in to_drop:
                continue
            score = fuzz.token_set_ratio(
                str(df.at[idx_i, 'job_title']) + str(df.at[idx_i, 'company_name']) + str(df.at[idx_i, 'full_description']),
                str(df.at[idx_j, 'job_title']) + str(df.at[idx_j, 'company_name']) + str(df.at[idx_j, 'full_description'])
            )
            if score > 95: # if similarity greater than 95% : drop the row 
                to_drop.add(idx_j)
df = df.drop(list(to_drop))
df = df.drop(columns="block")
df.to_csv("eures_jobs_deduped.csv", index=False)
