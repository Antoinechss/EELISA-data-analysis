import pandas as pd 

path = '/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/scraping/eures_jobs_deduped.csv'
df = pd.read_csv(path)

# Capital cities mapping for target countries
CAPITAL_MAPPING = {
    "BG": "Sofia",
    "HR": "Zagreb", 
    "CY": "Nicosia",
    "EE": "Tallinn",
    "GR": "Athens",
    "HU": "Budapest",
    "LV": "Riga",
    "LT": "Vilnius",
    "PL": "Warsaw",
    "PT": "Lisbon",
    "RO": "Bucharest",
    "ES": "Madrid"
}

def fill_missing_region(row):
    region = str(row['region']).strip()
    country_code = str(row['country_code']).upper()
    
    # If region is missing or empty, assign capital
    if not region or region.lower() in ['nan', 'none', '', 'null']:
        return CAPITAL_MAPPING.get(country_code, region)
    
    return region

# Apply the function to fill missing regions
df['region'] = df.apply(fill_missing_region, axis=1)

print(f"Updated regions for target countries with missing region data")
print(f"Dataset contains {len(df)} jobs")

# Save the updated dataset
df.to_csv(path, index=False)

