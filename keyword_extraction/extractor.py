import os
import json
import time
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

# =========================
# CONFIG
# =========================

DATASET_PATH = "/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/datasets/european_jobs.csv"
OUTPUT_PATH = "/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/outputs/job_extractions.jsonl"

MODEL_NAME = "gpt-4.1-mini"
SLEEP_BETWEEN_CALLS = 1.0  # seconds (safe rate)

MAX_DESC_CHARS = 8000  # safety truncation

# =========================
# LOAD ENV & CLIENT
# =========================

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# =========================
# LOCKED FRAMEWORKS
# =========================

DIGCOMP_LIST = [
    "Browsing, searching and filtering data, information and digital content",
    "Evaluating data, information and digital content",
    "Managing data, information and digital content",
    "Interacting through digital technologies",
    "Sharing through digital technologies",
    "Engaging in citizenship through digital technologies",
    "Collaborating through digital technologies",
    "Netiquette",
    "Managing digital identity",
    "Programming",
    "Copyright and licences",
    "Integrating and re-elaborating digital content",
    "Developing digital content",
    "Protecting devices",
    "Protecting personal data and privacy",
    "Protecting health and well-being",
    "Protecting the environment",
    "Solving technical problems",
    "Identifying needs and technological responses",
    "Creatively using digital technologies",
    "Identifying digital competence gaps"
]

GREENCOMP_LIST = [
    "Valuing sustainability",
    "Supporting fairness",
    "Promoting nature",
    "Systems thinking",
    "Problem framing",
    "Critical thinking",
    "Futures literacy",
    "Adaptability",
    "Exploratory thinking",
    "Political agency",
    "Collective action",
    "Individual initiative"
]

# =========================
# PROMPTS
# =========================

SYSTEM_PROMPT = """
You are an expert labour market analyst.

Rules:
- Return VALID JSON only.
- Do NOT invent information.
- If something is not explicitly mentioned, return an empty list or null.
- Use concise noun phrases.
- Hard skills are technical and task-specific.
- Soft skills are behavioural or interpersonal.
- Programming languages are NOT human languages.
- Only select digital and green competences from the provided lists.
- Do NOT paraphrase competence names.
- Only select a competence if it is clearly and unambiguously supported.
"""

def build_user_prompt(job_description: str) -> str:
    return f"""
Extract structured information from the job description below.

DIGITAL COMPETENCES (select only from this list):
{chr(10).join("- " + c for c in DIGCOMP_LIST)}

GREEN COMPETENCES (select only from this list):
{chr(10).join("- " + c for c in GREENCOMP_LIST)}

Return a JSON object with EXACTLY these fields:

hard_skills: list
tools: list
knowledge_domains: list
soft_skills: list
languages: list

education:
  level: one of ["none","bachelor","master","phd","other",null]
  field: string or null

digital_competences: list
green_competences: list

Job description:
\"\"\"
{job_description}
\"\"\"
"""

# =========================
# LOAD DATA
# =========================

df = pd.read_csv(DATASET_PATH)
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# =========================
# LOAD CACHE (SAFE RERUN)
# =========================

processed_ids = set()

if os.path.exists(OUTPUT_PATH):
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        for line in f:
            try:
                obj = json.loads(line)
                processed_ids.add(obj["job_id"])
            except Exception:
                continue

print(f"✔ Loaded {len(processed_ids)} already processed jobs")

# =========================
# EXTRACTION FUNCTION
# =========================

def extract_with_llm(description: str) -> dict:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(description)}
        ]
    )
    return json.loads(response.choices[0].message.content)

# =========================
# MAIN LOOP
# =========================

total = len(df)
processed = len(processed_ids)

print(f"▶ Starting extraction: {processed}/{total} already done")

with open(OUTPUT_PATH, "a", encoding="utf-8") as out:
    for idx, row in df.iterrows():

        job_id = row["job_id"]

        if job_id in processed_ids:
            continue

        start_time = time.time()

        print(f"[{processed + 1}/{total}] Processing job_id={job_id}...", end=" ")

        try:
            desc = str(row["full_description"])[:MAX_DESC_CHARS]
            extraction = extract_with_llm(desc)
            status = "ok"
        except Exception as e:
            extraction = {}
            status = "error"
            print(f"❌ ERROR: {e}")

        record = {
            "row_id": idx,
            "job_id": job_id,
            "job_title": row["job_title"],
            "country": row["country"],
            "isco_3": row["isco_3_digit"],
            "isco_3_label": row["isco_3_digit_label"],

            "hard_skills": extraction.get("hard_skills", []),
            "tools": extraction.get("tools", []),
            "knowledge_domains": extraction.get("knowledge_domains", []),
            "soft_skills": extraction.get("soft_skills", []),
            "languages": extraction.get("languages", []),

            "education_level": extraction.get("education", {}).get("level"),
            "education_field": extraction.get("education", {}).get("field"),

            "digital_competences": extraction.get("digital_competences", []),
            "green_competences": extraction.get("green_competences", []),

            "status": status
        }

        out.write(json.dumps(record, ensure_ascii=False) + "\n")
        out.flush()

        processed += 1
        elapsed = time.time() - start_time

        print(f"✓ done in {elapsed:.1f}s")

        time.sleep(SLEEP_BETWEEN_CALLS)

print("🎉 Extraction completed.")
