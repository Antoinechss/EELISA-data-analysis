import pandas as pd
import time
import json
from openai import OpenAI

client = OpenAI(api_key="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")

INPUT_CSV = "/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/datasets/european_jobs.csv"
OUTPUT_CSV = "/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/datasets/european_jobs_translated.csv"
CACHE_FILE = "translation_cache.json"

df = pd.read_csv(INPUT_CSV)
df["job_title_translated"] = ""

# Load cache to avoid duplicate translations
try:
    with open(CACHE_FILE, "r") as f:
        cache = json.load(f)
except:
    cache = {}


SYSTEM_PROMPT = """You are a translation engine specialized in job market terminology.
Translate all input text into English.
Keep the translation short, literal, and strictly aligned with the original meaning.
Do not summarize or explain.
Do not change the structure.
Do not infer missing words.
Do NOT output anything except the translated text.
"""

def translate(text):
    text = text.strip()
    if text == "":
        return ""
    
    # return cached translation if exists
    if text in cache:
        return cache[text]

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
        cache[text] = translation
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
