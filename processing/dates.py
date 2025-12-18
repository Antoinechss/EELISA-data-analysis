import pandas as pd


jobs_dataset = '/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/scraping/eures_additional_target_countries.csv'

df = pd.read_csv(jobs_dataset)

def parse_date(val):
    try:
        # Try to parse as integer timestamp (milliseconds)
        if pd.notnull(val) and str(val).isdigit() and len(str(val)) > 10:
            return pd.to_datetime(int(val), unit='ms')
        # Try to parse as normal date string
        return pd.to_datetime(val, errors='coerce')
    except Exception:
        return pd.NaT

df['date'] = df['date'].apply(parse_date)

# Keep only date part (remove time)
df['date'] = df['date'].dt.date

# Filter for dates >= 2025-01-01
df = df[df['date'] >= pd.to_datetime("2025-01-01").date()]

df.to_csv('dataset_dates_reformated.csv', index=False)

