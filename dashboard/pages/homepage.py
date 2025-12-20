import streamlit as st
import plotly.express as px
from PIL import Image

def show_job_offers_page(df):
    """Display the Job Offers Dataset page"""
    
    # Header with logos
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        try:
            eelisa_logo = Image.open('/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/dashboard/static/eelisa_logo.png')
            st.image(eelisa_logo, width=150)
        except:
            st.write("EELISA Logo")
    
    with col2:
        st.title("Job Offers Dataset")
    
    with col3:
        try:
            pep_logo = Image.open('/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/dashboard/static/PEP_logo.png')
            st.image(pep_logo, width=150)
        except:
            st.write("PEP Logo")
    
    # Introduction section
    st.markdown("---")
    st.header("About this Dataset")
    
    st.markdown("""
    The dataset **job offers.csv** was delivered to EELISA on **10.12.2025** for research purposes as part of a broader initiative to 
    analyse labour market trends, digital and green competencies, and emerging skill requirements across Europe. 
    
    It compiles job postings collected from multiple online recruitment platforms and harmonised to support cross-country comparison. 
    This document provides an overview of the dataset's structure, the methodology used to collect and normalise the 
    information, and the key variables included. 
    
    It also outlines the limitations inherent to web-scraped labour data, the assumptions applied during preprocessing, and 
    recommendations for safe and rigorous use of the dataset in research and policy analysis.
    
    **The objective** of this note is to ensure transparency, reproducibility, and a clear understanding of the dataset's scope so that 
    it can be reliably used by researchers, academic partners, and stakeholders involved in the **EELISA Data Science Mission**.
    """)
    
    st.markdown("---")
    
    # Dataset overview
    st.header("Dataset Overview")
    st.dataframe(df)
    
    # Add basic statistics
    st.subheader("Key Statistics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Jobs", len(df))
    with col2:
        st.metric("Total Columns", len(df.columns))
    with col3:
        if 'country' in df.columns:
            st.metric("Countries", df['country'].nunique())
        else:
            st.metric("Countries", "N/A")
    with col4:
        if 'field' in df.columns:
            st.metric("Fields", df['field'].nunique())
        else:
            st.metric("Fields", "N/A")
    
    # Add visualizations if data exists
    if not df.empty and len(df.columns) > 0:
        st.subheader("Data Visualizations")
        
        # Jobs by Country chart
        if 'country' in df.columns:
            fig = px.histogram(df, x='country', title="Job Distribution by Country")
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig, use_container_width=True)
        
        # Jobs by Field chart (if available)
        if 'field' in df.columns:
            fig2 = px.pie(df, names='field', title="Job Distribution by Field")
            st.plotly_chart(fig2, use_container_width=True)
        
