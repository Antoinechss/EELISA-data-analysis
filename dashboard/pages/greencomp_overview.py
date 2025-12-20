import streamlit as st
import pandas as pd
import base64

# GreenComp framework
GREENCOMP_FRAMEWORK = [
    ("Embodying sustainability values",
     ["Valuing sustainability", "Supporting fairness", "Promoting nature"]),
    ("Embracing complexity in sustainability",
     ["Systems thinking", "Problem framing", "Critical thinking"]),
    ("Envisioning sustainable futures",
     ["Futures literacy", "Adaptability", "Exploratory thinking"]),
    ("Acting for sustainability",
     ["Political agency", "Collective action", "Individual initiative"])
]

def show_greencomp_page():
    """Display the GreenComp overview page"""
    
    st.title("GreenComp Competence Framework")
    st.caption("European sustainability competence framework – 4 domains, 12 competences")
    
    # Add PDF download link
    col1, col2 = st.columns([3, 1])
    with col2:
        try:
            with open('/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/dashboard/static/GreenComp.pdf', "rb") as pdf_file:
                pdf_bytes = pdf_file.read()
                st.download_button(
                    label="📄 Read Official Documentation",
                    data=pdf_bytes,
                    file_name="GreenComp.pdf",
                    mime="application/pdf"
                )
        except FileNotFoundError:
            st.warning("📄 Official documentation not found")
    
    st.markdown("---")
    st.subheader("Sustainability Competence Domains")
    
    domain_descriptions = {
        "Embodying sustainability values": "Nurturing values that support sustainability and driving actions accordingly.",
        "Embracing complexity in sustainability": "Approaching sustainability challenges and opportunities in all their complexity.",
        "Envisioning sustainable futures": "Envisioning alternative sustainable futures by imagining and developing alternative scenarios.",
        "Acting for sustainability": "Acting as change agents in personal, local, national and global contexts."
    }
    
    for domain, description in domain_descriptions.items():
        with st.expander(f"{domain}"):
            st.write(description)
            competences = [comp for dom, comps in GREENCOMP_FRAMEWORK if dom == domain for comp in comps]
            for comp in competences:
                st.write(f"• **{comp}**")
