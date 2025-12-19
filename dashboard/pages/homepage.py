import streamlit as st
import plotly.express as px

def show_job_offers_page(df):
    """Display the Job Offers Dataset page"""
    st.title("Job Offers Dataset")
    st.dataframe(df)
    
    # Add basic statistics
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Jobs", len(df))
    with col2:
        st.metric("Total Columns", len(df.columns))
    
    # Add visualizations if data exists
    if not df.empty and len(df.columns) > 0:
        st.subheader("Data Overview")
        # Example chart - adjust column names based on your actual data
        if 'country' in df.columns:
            fig = px.histogram(df, x='country', title="Jobs by Country")
            st.plotly_chart(fig, use_container_width=True)