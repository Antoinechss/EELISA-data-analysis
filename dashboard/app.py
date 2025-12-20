import streamlit as st 
import pandas as pd 
import plotly.express as px
from pages.homepage import show_job_offers_page
from pages.greencomp_overview import show_greencomp_page
from pages.digcomp_overview import show_digcomp_page
from pages.digital_tools import show_digital_tools_page
from PIL import Image

# Page configs 
st.set_page_config(
    page_title="European Job Market Dashboard",
    layout="wide"
)

# Custom CSS for black background
st.markdown("""
<style>
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
    
    .stSidebar {
        background-color: #1A1A1A;
    }
    
    .stSidebar .stRadio > div {
        background-color: #1A1A1A;
        color: #FFFFFF;
    }
    
    .stDataFrame {
        background-color: #1A1A1A;
    }
    
    .stMetric {
        background-color: #1A1A1A;
        padding: 10px;
        border-radius: 5px;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important;
    }
    
    .stExpander {
        background-color: #1A1A1A;
        border: 1px solid #333333;
    }
    
    .stButton > button {
        background-color: #333333;
        color: #FFFFFF;
        border: 1px solid #555555;
    }
    
    .stButton > button:hover {
        background-color: #555555;
        border: 1px solid #777777;
    }
</style>
""", unsafe_allow_html=True)

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
        "GreenComp"
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

# ---- Digital Tools ----
## TODO

# ---- Education ----
## TODO
