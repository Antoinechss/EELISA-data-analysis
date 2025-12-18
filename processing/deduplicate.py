import pandas as pd
from rapidfuzz import fuzz

jobs_dataset = '/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/scraping/dataset_filtered.csv'
df = pd.read_csv(jobs_dataset)

print(f"Original dataset: {len(df)} jobs")

# ------------------------
# Removing duplicate job offers using fuzzy matching 
# ------------------------
df = df.drop_duplicates(subset=["job_title", "company_name", "full_description"])
print(f"After exact duplicate removal: {len(df)} jobs")

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

print(f"Fuzzy duplicates found: {len(to_drop)} jobs")

df = df.drop(list(to_drop))
df = df.drop(columns="block")

print(f"Final dataset after deduplication: {len(df)} jobs")
print(f"Total duplicates removed: {pd.read_csv(jobs_dataset).shape[0] - len(df)} jobs")

df.to_csv("eures_jobs_deduped.csv", index=False)
