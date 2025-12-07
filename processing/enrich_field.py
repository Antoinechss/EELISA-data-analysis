import pandas as pd
from openai import OpenAI
import time
import json
import os
from tqdm import tqdm  # progress bar


# -----------------------------
# CONFIG
# -----------------------------
INPUT_CSV = 'input_path'
OUTPUT_CSV = 'output_path'
CACHE_FILE = "inferred_fields.json"

MODEL_NAME = "gpt-4.1-mini"   # most stable available to your account


# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv(INPUT_CSV)

# Create field column if missing
if "job_field" not in df.columns:
    df["job_field"] = ""

# Load cache
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r") as f:
        cache = json.load(f)
else:
    cache = {}


# -----------------------------
# OPENAI CLIENT
# -----------------------------
client = OpenAI()


# -----------------------------
# SYSTEM PROMPT (SHORT & STABLE)
# -----------------------------
SYSTEM_PROMPT = """
Classify this job description into EXACTLY one field from the list below.
Return ONLY valid JSON.

FIELDS:
1. Data Science & Analytics
2. Artificial Intelligence & Machine Learning
3. Software Engineering & Development
4. Cybersecurity & Information Security
5. Cloud, DevOps & Systems Engineering
6. Telecommunications & Networking
7. Internet of Things (IoT) & Embedded Systems
8. Robotics & Automation
9. Electrical & Electronics Engineering
10. Mechanical Engineering
11. Civil & Structural Engineering
12. Chemical & Process Engineering
13. Materials Science & Materials Engineering
14. Aerospace & Aeronautical Engineering
15. Energy Engineering (Nuclear, Oil & Gas)
16. Environmental & Sustainability Engineering
17. Earth & Geosciences (Geology, Geophysics, Remote Sensing)
18. Biomedical & Biotech Engineering
19. Bioinformatics & Computational Biology
20. Manufacturing Engineering & Industry 4.0
21. Supply Chain, Operations & Industrial Engineering
22. Product Design, UX, and HCI
23. Quantum Computing & Quantum Engineering
24. Extended Reality (AR/VR/XR) & Immersive Technologies
25. Computer Graphics, Vision & Multimedia
26. Automotive & Transportation Engineering
27. Marine & Naval Engineering
28. Mining & Metallurgical Engineering
29. Agritech & Food Engineering
30. Research & Academia
31. Renewable Energy Engineering

If none applies, return "Non Technical".

OUTPUT FORMAT STRICT:
{
  "field": "..."
}
"""


# -----------------------------
# JSON PARSER + FALLBACK
# -----------------------------
def extract_field_from_response(raw):
    """
    Guaranteed recovery of a single field even when GPT outputs noisy text.
    """
    # Try normal JSON parsing
    try:
        data = json.loads(raw)
        if "field" in data:
            return data["field"]
    except:
        pass

    # Extract first quoted string as fallback
    import re
    matches = re.findall(r'"([^"]+)"', raw)
    if matches:
        return matches[0]

    return None


# -----------------------------
# INFERENCE: ONE ROW AT A TIME
# -----------------------------
def infer_field(description):
    """
    Stable single-item classification with caching and fallback parsing.
    """

    # Return from cache if already known
    if description in cache:
        return cache[description]

    while True:
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": description}
                ]
            )
        except Exception as e:
            print("⚠️ API error – retrying in 5 seconds:", e)
            time.sleep(5)
            continue

        raw = response.choices[0].message.content.strip()
        field = extract_field_from_response(raw)

        if field:
            cache[description] = field
            return field
        print("Invalid output, retrying...")
        time.sleep(1)


# -----------------------------
# MAIN LOOP 
# -----------------------------
print("Starting job field inference…")

for i in tqdm(range(len(df)), desc="Processing rows"):
    
    desc = str(df.loc[i, "full_description"])

    # Skip if already filled
    if df.loc[i, "job_field"] != "" and desc in cache:
        continue

    # Infer field
    field = infer_field(desc)
    df.loc[i, "job_field"] = field

    # Autosave every 50 rows
    if i % 50 == 0:
        df.to_csv(OUTPUT_CSV, index=False)
        with open(CACHE_FILE, "w") as f:
            json.dump(cache, f)

# Final save
df.to_csv(OUTPUT_CSV, index=False)
with open(CACHE_FILE, "w") as f:
    json.dump(cache, f)

print("All job fields inferred successfully!")
print("Saved to:", OUTPUT_CSV)
