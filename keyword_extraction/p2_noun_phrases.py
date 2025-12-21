import spacy
import re
import pandas as pd

"""
First gross extraction of noun phrases
Maximum recall
Full traceability
One-pass extraction locked
"""

nlp = spacy.load("en_core_web_sm") # Load english version of NLP model 

corpus = '/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/keyword_extraction/cleaned_corpus.csv'
corpus_df = pd.read_csv(corpus)

# Stop noun phrases made only of stopwords / punctuation
STOPLIKE_RE = re.compile(r"^[\W_]+$")


def extract_noun_phrases(text: str):
    doc = nlp(text)
    phrases = []
    for chunk in doc.noun_chunks:
        p = chunk.text.lower().strip()
        p = re.sub(r"\s+", " ", p)
        p = p.strip(" -–—,.;:()[]{}")
        if len(p) < 3:
            continue
        if STOPLIKE_RE.match(p):
            continue
        if p.isdigit():
            continue
        phrases.append(p)
    return phrases


rows = []
for _, r in corpus_df.iterrows():
    nps = extract_noun_phrases(r["clean_description"])
    for np in nps:
        rows.append({
            "job_id": r["job_id"],
            "country": r["country"],
            "isco_3_digit_label": r["isco_3_digit_label"],
            "noun_phrase": np
        })

np_occ = pd.DataFrame(rows)

print("Jobs in corpus:", len(corpus_df))
print("Total noun-phrase occurrences:", len(np_occ))
print("\nTop 20 noun phrases:\n")
print(np_occ["noun_phrase"].value_counts().head(20))

np_occ.to_csv("noun_phrase_occurrences.csv", index=False)
