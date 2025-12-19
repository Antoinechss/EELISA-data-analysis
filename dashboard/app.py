import streamlit as st 
import pandas as pd 
import plotly.express as px
from pages.homepage import show_job_offers_page

dataset_path = '/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/datasets/european_jobs.csv'
df = pd.read_csv(dataset_path)

# Page configs 
st.set_page_config(
    page_title="European Job Market Dashboard",
    layout="wide"
)
# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Job Offers Dataset",
        "DigComp",
        "GreenComp "
    ]
)

# ---- Job Offers Dataset ----
if page == "Job Offers Dataset":
    show_job_offers_page(df)

# ---- DigComp ----
elif page == "DigComp":
    st.title("DigComp Framework")
    # Add DigComp content here

# ---- GreenComp ----
elif page == "GreenComp ":
    st.title("GreenComp Framework")
    # Add GreenComp content here
