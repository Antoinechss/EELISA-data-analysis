import pandas as pd 
isco_classification = '/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/processing/field_classification/ISCO_classification.xlsx'

df = pd.read_excel(isco_classification)
isco3 = df[['3_digit_code', '3_digit_label']]
isco3 = isco3.drop_duplicates().reset_index(drop=True)
isco3.to_csv('ISCO_3_digits.csv', index=False)