import pandas as pd
import time
import json
from openai import OpenAI

client = OpenAI(api_key="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")

INPUT_CSV = "/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/datasets/european_jobs.csv"
OUTPUT_CSV = "/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/datasets/european_jobs_translated.csv"

df = pd.read_csv(INPUT_CSV)
df["job_title_translated"] = ""


SYSTEM_PROMPT = """You are a professional translation engine specialized in multilingual job-market texts.
Translate the following job descriptions into English.
Keep the translation literal, accurate, and faithful to the original meaning.
Preserve structure, bullet points, and formatting as much as possible.
Do not summarize.
Do not rewrite or improve the text.
Do not omit anything.
Output only the translations, in the same list order as the inputs.
"""

def translate(text):
    text = text.strip()
    if text == "":
        return ""

    # request API
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text}
            ]
        )

        translation = response.choices[0].message.content.strip()
        return translation

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
        return translate(text)  # retry


# Apply to all rows 
for i, row in df.iterrows():
    original = str(row["job_title"])
    translated = translate(original)
    df.at[i, "job_title_translated"] = translated

    # Save progress every 500 rows
    if i % 500 == 0:
        print(f"Progress: {i}/{len(df)} rows")
        df.to_csv(OUTPUT_CSV, index=False)
        with open(CACHE_FILE, "w") as f:
            json.dump(cache, f)

df.to_csv(OUTPUT_CSV, index=False)
with open(CACHE_FILE, "w") as f:
    json.dump(cache, f)

print("Translation completed!")
