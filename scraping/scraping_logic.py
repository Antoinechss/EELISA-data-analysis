"""
Main scraping logic with keywords used for both EURES and yenibris websites 
"""

from bs4 import BeautifulSoup
from nuts import COUNTRY_CODE_TO_NAME, NUTS_REGIONS
from scraping.config import DOMAIN_PATTERNS

# -----------------------------
# HTML PARSING LOGIC
# -----------------------------

def clean_html(html_text: str | None) -> str:
    if not html_text:
        return ""
    soup = BeautifulSoup(html_text, "html.parser")
    return soup.get_text(" ", strip=True)


# -----------------------------
# DOMAIN CLASSIFIER : Later improved with GPT-4.1 mini LLM 
# -----------------------------
def classify_domain(title: str | None, description: str | None) -> str:
    text = (title or "").lower() + " " + (description or "").lower()
    for domain, patterns in DOMAIN_PATTERNS:
        if any(p in text for p in patterns):
            return domain
    return "Other / Undefined"


# -----------------------------
# Helper functions 
# -----------------------------
def extract_company_from_text(text: str) -> str | None:
    """
    Extracts likely company names from job descriptions using multilingual patterns.
    Returns None if nothing matches.
    """

    if not text:
        return None

    text_clean = text.replace("\n", " ").strip()

    # --- 1. Most common multilingual patterns ---
    patterns = [
        r"for\s+([A-Z][A-Za-z0-9&\-\s']+)",                     # for Airbus
        r"at\s+([A-Z][A-Za-z0-9&\-\s']+)",                      # at Siemens
        r"join\s+([A-Z][A-Za-z0-9&\-\s']+)",                    # join L'Oréal
        r"with\s+([A-Z][A-Za-z0-9&\-\s']+)",                    # with BMW

        r"chez\s+([A-Z][A-Za-z0-9&\-\s']+)",                    # chez Dior (French)
        r"pour\s+([A-Z][A-Za-z0-9&\-\s']+)",                    # pour Chanel / pour Airbus

        # Recruiter phrasing
        r"for our client\s+([A-Z][A-Za-z0-9&\-\s']+)",          # for our client L'Oréal
        r"pour le compte de\s+([A-Z][A-Za-z0-9&\-\s']+)",       # pour le compte de Hermès
        r"en nombre de\s+([A-Z][A-Za-z0-9&\-\s']+)",            # en nombre de X
    ]

    for pattern in patterns:
        match = re.search(pattern, text_clean, flags=re.IGNORECASE)
        if match:
            name = match.group(1).strip()

            # Clean trailing junk like commas or dots
            name = re.sub(r"[.,;:]+$", "", name)

            # Avoid false positives like "our team", "the company"
            if len(name.split()) <= 6 and not name.lower().startswith(("the ", "our ")):
                return name

    return None

def infer_country_from_location_map(location_map: dict | None) -> str | None:
    if not location_map:
        return None
    try:
        code = next(iter(location_map.keys()))
        return COUNTRY_CODE_TO_NAME.get(code.lower(), code.upper())
    except StopIteration:
        return None
    
def extract_region_from_location_map(location_map: dict | None) -> str | None:
    """
    Convert NUTS location code (FRL04) to Region name (Provence-Alpes-Côte d'Azur).
    """
    if not location_map:
        return None

    try:
        country_code = next(iter(location_map.keys()))
        nuts_list = location_map[country_code]

        if not nuts_list:
            return None

        # reads the first 3 characters of the string
        nuts_code = nuts_list[0]       
        nuts_prefix = nuts_code[:3]   

        return NUTS_REGIONS.get(nuts_prefix, nuts_prefix)
    except Exception:
        return None

