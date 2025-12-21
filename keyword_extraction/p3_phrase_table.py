import pandas as pd
import re

# ----------------------------
# Load noun phrase occurrences
# ----------------------------
np_occ = pd.read_csv("noun_phrase_occurrences.csv")

print("Loaded noun phrase occurrences:", np_occ.shape)

# ----------------------------
# Basic linguistic filters
# (conservative, no bias)
# ----------------------------

PRONOUNS = {
    "i","you","he","she","it","we","they",
    "who","which","that","this","these","those"
}

DETERMINERS = {
    "a","an","the","this","that","these","those"
}

LANGUAGES = {
    "english", "french", "german", "spanish", "italian",
    "portuguese", "dutch", "polish", "romanian",
    "hungarian", "czech", "slovak", "slovenian",
    "swedish", "danish", "finnish", "norwegian",
    "greek", "turkish"
}

def is_bad_phrase(p) -> bool:
    if not isinstance(p, str):
        return True

    p = p.strip().lower()
    if not p:
        return True

    # 🔒 Always keep languages
    if p in LANGUAGES:
        return False

    tokens = p.split()

    PRONOUNS = {
        "i","you","he","she","it","we","they",
        "who","which","that","this","these","those"
    }

    DETERMINERS = {
        "a","an","the","this","that","these","those"
    }

    WH_WORDS = {"what", "who", "which", "when", "where", "why", "how"}

    if len(tokens) == 1 and tokens[0] in PRONOUNS:
        return True

    if len(tokens) == 1 and tokens[0] in WH_WORDS:
        return True

    if tokens[0] in DETERMINERS or tokens[-1] in DETERMINERS:
        return True

    if p in {"the position", "this role", "the role", "a team"}:
        return True

    return False



# Apply filter
np_occ["keep"] = ~np_occ["noun_phrase"].apply(is_bad_phrase)
np_occ_filt = np_occ[np_occ["keep"]].copy()

print("After filtering:", np_occ_filt.shape)

phrase_table = (
    np_occ_filt
    .groupby("noun_phrase")
    .agg(
        frequency=("job_id", "count"),
        example_job_id=("job_id", "first")
    )
    .reset_index()
    .sort_values("frequency", ascending=False)
)

print("\nTop 20 filtered noun phrases:")
print(phrase_table.head(20))
phrase_table.to_csv("phrase_candidates.csv", index=False)
