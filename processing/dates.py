import pandas as pd

jobs_dataset = 'path'
df = pd.read_csv(jobs_dataset)

# ------------------------
# Translating timestamp to proper  YYYY-MM-DD format 
# ------------------------

def parse_date(val):
    try:
        # Try to parse as integer timestamp (milliseconds)
        if pd.notnull(val) and str(val).isdigit() and len(str(val)) > 10:
            return pd.to_datetime(int(val), unit='ms')
        # Try to parse as normal date string
        return pd.to_datetime(val, errors='coerce')
    except Exception:
        return pd.NaT

df['date'] = df['date'].apply(parse_date).dt.strftime('%Y-%m-%d')
df.to_csv(jobs_dataset, index=False)

# ------------------------
# Restrict to recent job posts (before the 01.01.2025)
# ------------------------
def parse_date(val):
    try:
        if pd.notnull(val) and str(val).isdigit() and len(str(val)) > 10:
            return pd.to_datetime(int(val), unit='ms')
        return pd.to_datetime(val, errors='coerce')
    except Exception:
        return pd.NaT

df['date'] = df['date'].apply(parse_date)
df = df[df['date'] >= pd.to_datetime("2025-01-01")]


