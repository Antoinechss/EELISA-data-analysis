import streamlit as st
import pandas as pd

# DigComp competence framework : 5 domains and 21 competences
DIGCOMP_FRAMEWORK = [("Information and digital literacy", 
                      ["Browsing, searching and filtering data, information and digital content", 
                       "Evaluating data, information and digital content", 
                       "Managing data, information and digital content"]),
                     ("Communication and collaboration",
                      ["Interacting through digital technologies", 
                       "Sharing through digital technologies", 
                       "Engaging in citizenship through digital technologies", 
                       "Collaborating through digital technologies", 
                       "Netiquette",
                       "Managing digital identity"]),
                     ("Digital content creation",
                      ["Programming","Copyright and licences","Integrating and re-elaborating digital content","Developing digital content"]),
                     ("Safety",
                      ["Protecting devices",
                       "Protecting personal data and privacy",
                       "Protecting health and well-being",
                       "Protecting the environment"]),
                     ("Problem-solving",
                      ["Solving technical problems", 
                       "Identifying needs and technological responses", 
                       "Creatively using digital technologies", 
                       "Identifying digital competence gaps"])
]

def show_digcomp_page():
    """Display the DigComp overview page"""
    
    st.title("DigComp Competence Framework")
    st.caption("European digital competence framework – 5 domains, 21 competences")
    
    # Add PDF download link
    col1, col2 = st.columns([3, 1])
    with col2:
        try:
            with open('/Users/antoinechosson/Desktop/EELISA/EELISA-Data-analysis/dashboard/static/DigComp.pdf', "rb") as pdf_file:
                pdf_bytes = pdf_file.read()
                st.download_button(
                    label="📄 Read Official Documentation",
                    data=pdf_bytes,
                    file_name="DigComp.pdf",
                    mime="application/pdf"
                )
        except FileNotFoundError:
            st.warning("📄 Official documentation not found")
    
    st.markdown("---")
    st.subheader("Digital Competence Domains")
    
    domain_descriptions = {
        "Information and digital literacy": "Articulate information needs, locate and retrieve digital data, information and content.",
        "Communication and collaboration": "Communicate in digital environments, share resources through online tools, connect and collaborate with others.",
        "Digital content creation": "Create and edit digital content in different formats, express oneself through digital means.",
        "Safety": "Protect devices, personal data, privacy and digital identity, use technology safely and sustainably.",
        "Problem-solving": "Solve problems and make informed decisions about the most appropriate digital tools according to the purpose or need."
    }
    
    for domain, description in domain_descriptions.items():
        with st.expander(f"{domain}"):
            st.write(description)
            competences = [comp for dom, comps in DIGCOMP_FRAMEWORK if dom == domain for comp in comps]
            for comp in competences:
                st.write(f"• **{comp}**")