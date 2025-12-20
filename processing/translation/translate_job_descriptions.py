import pandas as pd
import time
import json
import re
import os
from dotenv import load_dotenv
from openai import OpenAI

# -----------------------------
# CONFIG
# -----------------------------

# Load environment variables
load_dotenv()

# Use the environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# CHANGE: Update input and output paths
INPUT_CSV = "/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/datasets/european_jobs_2.csv"
OUTPUT_CSV = "/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/datasets/european_jobs_2_translated.csv"
CACHE_FILE = "description_translation_cache_v2.json"  # CHANGE: Different cache file

BATCH_SIZE = 5   # safe for gpt-4o-mini  # CHANGE: Fix model name

# -----------------------------
# LOAD DATA + CACHE
# -----------------------------

df = pd.read_csv(INPUT_CSV)

# CHANGE: Check if description column exists and what it's called
if "full_description" not in df.columns:
    print("Available columns:", df.columns.tolist())
    print("ERROR: 'full_description' column not found!")
    exit()

if "job_description_translated" not in df.columns:
    df["job_description_translated"] = ""

try:
    with open(CACHE_FILE, "r") as f:
        cache = json.load(f)
except:
    cache = {}


# -----------------------------
# SYSTEM PROMPT (STRICT JSON)
# -----------------------------

SYSTEM_PROMPT = """
You are a translation engine for job-market texts.

Translate the following job descriptions into English.

Return your output strictly as VALID JSON in the EXACT format:

{
  "translations": [
    "... translation of item 1 ...",
    "... translation of item 2 ...",
    "... translation of item 3 ...",
    "... translation of item 4 ...",
    "... translation of item 5 ..."
  ]
}

Rules:
- The number of items MUST match exactly the number of inputs.
- No explanations, no commentary, no extra keys.
- Do NOT modify the JSON structure.
- Do NOT add trailing commas.
- Keep translations literal and faithful.
- Preserve formatting, lists, and structure.
"""


# -----------------------------
# PARSE JSON OUTPUT
# -----------------------------

def parse_json_output(text):
    try:
        data = json.loads(text)
        if "translations" in data and isinstance(data["translations"], list):
            return data["translations"]
    except Exception:
        pass
    return None


# -----------------------------
# TRANSLATE BATCH 
# -----------------------------
def translate_batch(text_list):
    # Reuse cached translations where possible
    cached = []
    missing = []

    for txt in text_list:
        if txt in cache:
            cached.append(cache[txt])
        else:
            cached.append(None)
            missing.append(txt)

    # Nothing to translate
    if len(missing) == 0:
        return cached

    # Build the numbered input for missing items
    user_input = "\n".join([f"{i+1}. {t}" for i, t in enumerate(missing)])

    # Add debug: show what we're sending
    print(f"Translating {len(missing)} items:")
    for i, item in enumerate(missing):
        print(f"  {i+1}. {item[:50]}...")

    # Retry loop
    retry_count = 0
    while retry_count < 3:  # Limit retries
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_input}
                ]
            )
        except Exception as e:
            print("API error, retrying in 5s:", e)
            time.sleep(5)
            continue

        text = response.choices[0].message.content.strip()
        
        # DEBUG: Show raw response
        print(f"Raw API response ({len(text)} chars):")
        print(text[:200] + "..." if len(text) > 200 else text)
        print("="*50)
        
        results = parse_json_output(text)

        # If JSON invalid, retry
        if (
            results is None
            or not isinstance(results, list)
            or len(results) != len(missing)
        ):
            retry_count += 1
            print(f"JSON mismatch (attempt {retry_count}): expected {len(missing)} got {len(results) if results else 'None'}")
            if retry_count < 3:
                print("Retrying batch...")
                time.sleep(2)
                continue
            else:
                print("Max retries reached. Skipping batch.")
                return ["[TRANSLATION_FAILED]"] * len(text_list)

        # Valid JSON and correct size → break retry loop
        break

    # Merge new translations with cached ones
    final = []
    idx_new = 0

    for original, cval in zip(text_list, cached):
        if cval is not None:
            final.append(cval)
        else:
            translation = results[idx_new]
            cache[original] = translation
            final.append(translation)
            idx_new += 1

    return final


# -----------------------------
# MAIN LOOP
# -----------------------------

total_rows = len(df)

for start in range(0, total_rows, BATCH_SIZE):
    end = min(start + BATCH_SIZE, total_rows)

    originals = df.loc[start:end-1, "full_description"].astype(str).tolist()
    translations = translate_batch(originals)

    df.loc[start:end-1, "job_description_translated"] = translations

    # Save progress every 200 rows
    if start % 200 == 0:
        print(f"Progress: {start}/{total_rows} rows")
        df.to_csv(OUTPUT_CSV, index=False)
        with open(CACHE_FILE, "w") as f:
            json.dump(cache, f)

# Final save
df.to_csv(OUTPUT_CSV, index=False)
with open(CACHE_FILE, "w") as f:
    json.dump(cache, f)

print("Translation of job descriptions completed successfully!")
