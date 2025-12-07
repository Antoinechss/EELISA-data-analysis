from nuts import NUTS_REGIONS, NUTS_COORDINATES
import pandas as pd

jobs_dataset = 'input_path'
output_path = 'output_path'
df = pd.read_csv(jobs_dataset)

def get_region_code(region_name):
    for key, value in NUTS_REGIONS.items():
        if value == region_name:
            return key
    return None


def get_coordinates(region_name):
    region_token = get_region_code(region_name)
    if region_token and region_token in NUTS_COORDINATES:
        return NUTS_COORDINATES[region_token]
    return (None, None)


# Assign coordinates column using apply
df['coordinates'] = df['region'].apply(get_coordinates)

df.to_csv(output_path, index=False)

