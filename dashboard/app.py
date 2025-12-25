import streamlit as st 
import pandas as pd 
import plotly.express as px
from pages.homepage import show_job_offers_page
from pages.greencomp_overview import show_greencomp_page
from pages.digcomp_overview import show_digcomp_page
from pages.digital_tools import show_digital_tools_page
from pages.digcomp_profiles import show_digcomp_profiles_page 
from PIL import Image

# Page configs 
st.set_page_config(
    page_title="European Job Market Dashboard",
    layout="wide"
)
dataset_path = '/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/datasets/european_jobs.csv'
df = pd.read_csv(dataset_path)

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Job Offers Dataset",
        "Digital Tools Analysis",
        "DigComp",
        "GreenComp", 
        "DigComp Profiles"
    ]
)

# ---- Job Offers Dataset ----
if page == "Job Offers Dataset":
    show_job_offers_page(df)

# ---- Digital Tools Analysis ----
elif page == "Digital Tools Analysis":
    show_digital_tools_page(df)

# ---- DigComp ----
elif page == "DigComp":
    show_digcomp_page()

# ---- GreenComp ----
elif page == "GreenComp":
    show_greencomp_page()

# ---- DigComp Profiles ----
elif page == "DigComp Profiles":
    show_digcomp_profiles_page()

# ---- Digital Tools ----
## TODO

# ---- Education ----
## TODO
