import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import re
from collections import Counter
from itertools import chain

# Your TECH_TOOLS dictionary (same as original)
TECH_TOOLS = {
    # =======================
    # Office & Productivity
    # =======================
    "excel": ["excel", "ms excel", "microsoft excel"],
    "powerpoint": ["powerpoint", "ppt", "pptx", "ms powerpoint"],
    "word": ["word", "ms word", "microsoft word"],
    "outlook": ["outlook", "ms outlook"],
    "onenote": ["onenote"],
    "access": ["access", "ms access"],
    "google_sheets": ["google sheets", "g sheets"],
    "google_docs": ["google docs"],
    "google_slides": ["google slides"],

    # =======================
    # Data & Analytics
    # =======================
    "sql": ["sql", "mysql", "postgresql", "sqlite", "oracle sql"],
    "python": ["python", "pandas", "numpy", "scipy"],
    "r": ["r", "rstudio"],
    "sas": ["sas"],
    "spss": ["spss"],
    "stata": ["stata"],
    "matlab": ["matlab"],
    "excel_vba": ["vba", "excel vba"],
    "power_bi": ["power bi", "powerbi"],
    "tableau": ["tableau"],
    "looker": ["looker"],
    "qlik": ["qlik", "qlikview", "qliksense"],
    "databricks": ["databricks"],
    "bigquery": ["bigquery", "google bigquery"],

    # =======================
    # Programming Languages
    # =======================
    "java": ["java"],
    "c": ["c programming", "language c"],
    "cpp": ["c++"],
    "csharp": ["c#", "c sharp"],
    "javascript": ["javascript", "js"],
    "typescript": ["typescript"],
    "php": ["php"],
    "go": ["go", "golang"],
    "rust": ["rust"],
    "swift": ["swift"],
    "kotlin": ["kotlin"],
    "scala": ["scala"],

    # =======================
    # Web Development
    # =======================
    "html": ["html"],
    "css": ["css"],
    "react": ["react", "reactjs"],
    "angular": ["angular"],
    "vue": ["vue", "vuejs"],
    "nodejs": ["node.js", "nodejs"],
    "django": ["django"],
    "flask": ["flask"],
    "spring": ["spring", "spring boot"],
    "laravel": ["laravel"],
    "wordpress": ["wordpress", "wp"],
    "shopify": ["shopify"],

    # =======================
    # Databases
    # =======================
    "mysql": ["mysql"],
    "postgresql": ["postgresql", "postgres"],
    "oracle": ["oracle"],
    "mongodb": ["mongodb"],
    "redis": ["redis"],
    "cassandra": ["cassandra"],
    "firebase": ["firebase"],
    "elasticsearch": ["elasticsearch"],

    # =======================
    # Cloud & DevOps
    # =======================
    "aws": ["aws", "amazon web services"],
    "azure": ["azure", "microsoft azure"],
    "gcp": ["gcp", "google cloud"],
    "docker": ["docker"],
    "kubernetes": ["kubernetes", "k8s"],
    "terraform": ["terraform"],
    "ansible": ["ansible"],
    "jenkins": ["jenkins"],
    "github_actions": ["github actions"],
    "ci_cd": ["ci/cd", "continuous integration"],

    # =======================
    # Version Control
    # =======================
    "git": ["git"],
    "github": ["github"],
    "gitlab": ["gitlab"],
    "bitbucket": ["bitbucket"],

    # =======================
    # Project Management & Collaboration
    # =======================
    "jira": ["jira"],
    "confluence": ["confluence"],
    "trello": ["trello"],
    "asana": ["asana"],
    "monday": ["monday", "monday.com"],
    "notion": ["notion"],
    "slack": ["slack"],
    "teams": ["microsoft teams", "ms teams"],
    "zoom": ["zoom"],
    "google_workspace": ["google workspace"],

    # =======================
    # CRM / ERP / Business Tools
    # =======================
    "salesforce": ["salesforce"],
    "sap": ["sap"],
    "oracle_erp": ["oracle erp"],
    "workday": ["workday"],
    "dynamics_365": ["dynamics 365"],
    "hubspot": ["hubspot"],
    "zoho": ["zoho"],

    # =======================
    # Marketing & Analytics Tools
    # =======================
    "google_analytics": ["google analytics", "ga4"],
    "google_ads": ["google ads", "adwords"],
    "meta_ads": ["meta ads", "facebook ads"],
    "seo_tools": ["seo", "semrush", "ahrefs"],
    "mailchimp": ["mailchimp"],
    "salesforce_marketing_cloud": ["marketing cloud"],
    "crm_analytics": ["crm analytics"],

    # =======================
    # AI / ML / Data Science
    # =======================
    "tensorflow": ["tensorflow"],
    "pytorch": ["pytorch"],
    "scikit_learn": ["scikit-learn", "sklearn"],
    "keras": ["keras"],
    "opencv": ["opencv"],
    "huggingface": ["huggingface"],

    # =======================
    # Cybersecurity
    # =======================
    "iso_27001": ["iso 27001"],
    "penetration_testing": ["penetration testing", "pentesting"],
    "firewalls": ["firewalls"],
    "siem": ["siem"],
    "iam": ["identity and access management", "iam"],

    # =======================
    # Green / Sustainability Tech
    # =======================
    "energy_management": ["energy management"],
    "carbon_accounting": ["carbon accounting", "carbon footprint"],
    "lca": ["lca", "life cycle assessment"],
    "environmental_reporting": ["environmental reporting"],
    "sustainability_software": ["sustainability software"],
}

def extract_tech_tools(text, tech_dict):
    """Extract technical tools mentioned in text"""
    text = str(text).lower()
    found_tools = set()

    for tool, variants in tech_dict.items():
        for v in variants:
            pattern = r"\b" + re.escape(v) + r"\b"
            if re.search(pattern, text):
                found_tools.add(tool)
                break

    return list(found_tools)

def show_digital_tools_page(df):
    """Display the Digital Tools analysis page"""
    
    st.title("🔧 Digital Tools Analysis")
    st.caption("Most mentioned technical tools and technologies in job descriptions")
    
    # Process the data
    with st.spinner("Analyzing technical tools in job descriptions..."):
        df["tech_tools"] = df["full_description"].apply(
            lambda x: extract_tech_tools(str(x), TECH_TOOLS)
        )
        
        # Count tool occurrences
        tool_counts = Counter(chain.from_iterable(df["tech_tools"]))
        
    if not tool_counts:
        st.warning("No technical tools found in the job descriptions.")
        return
    
    # Get top tools
    top_30_tools = tool_counts.most_common(30)
    treemap_df = pd.DataFrame(top_30_tools, columns=["tool", "count"])
    
    # Create treemap using plotly
    fig = go.Figure(go.Treemap(
        labels=[f"{tool}<br>{count} jobs" for tool, count in zip(treemap_df["tool"], treemap_df["count"])],
        values=treemap_df["count"],
        parents=[""] * len(treemap_df),
        textinfo="label+value",
        textposition="middle center",
        marker=dict(
            colorscale="Viridis",
            colorbar=dict(title="Job Count")
        )
    ))
    
    fig.update_layout(
        title="Top 30 Most Mentioned Technical Tools",
        font=dict(size=12),
        height=600,
        margin=dict(t=50, l=25, r=25, b=25)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Show statistics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Unique Tools", len(tool_counts))
    
    with col2:
        total_mentions = sum(tool_counts.values())
        st.metric("Total Tool Mentions", total_mentions)
    
    with col3:
        jobs_with_tools = len([tools for tools in df["tech_tools"] if tools])
        percentage = (jobs_with_tools / len(df)) * 100
        st.metric("Jobs with Tools", f"{percentage:.1f}%")
    
    # Show top tools table
    st.subheader("Top 20 Technical Tools")
    top_20_df = pd.DataFrame(tool_counts.most_common(20), columns=["Tool", "Job Mentions"])
    top_20_df["Percentage"] = (top_20_df["Job Mentions"] / len(df) * 100).round(1)
    
    st.dataframe(
        top_20_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Tool": "Technical Tool",
            "Job Mentions": st.column_config.NumberColumn("Job Mentions", format="%d"),
            "Percentage": st.column_config.NumberColumn("% of Jobs", format="%.1f%%")
        }
    )
    
    # Tool categories breakdown
    st.subheader("Tools by Category")
    
    categories = {
        "Programming Languages": ["python", "java", "javascript", "typescript", "php", "c", "cpp", "csharp", "go", "rust", "swift", "kotlin", "scala"],
        "Data & Analytics": ["sql", "python", "r", "sas", "spss", "stata", "matlab", "power_bi", "tableau", "looker", "qlik", "databricks", "bigquery"],
        "Cloud & DevOps": ["aws", "azure", "gcp", "docker", "kubernetes", "terraform", "ansible", "jenkins", "github_actions", "ci_cd"],
        "Office & Productivity": ["excel", "powerpoint", "word", "outlook", "onenote", "access", "google_sheets", "google_docs", "google_slides"],
        "Web Development": ["html", "css", "react", "angular", "vue", "nodejs", "django", "flask", "spring", "laravel", "wordpress", "shopify"]
    }
    
    category_counts = {}
    for category, tools in categories.items():
        category_count = sum(tool_counts.get(tool, 0) for tool in tools)
        if category_count > 0:
            category_counts[category] = category_count
    
    if category_counts:
        # Create bar chart for categories
        fig_cat = px.bar(
            x=list(category_counts.keys()),
            y=list(category_counts.values()),
            title="Tool Mentions by Category",
            labels={"x": "Category", "y": "Total Mentions"}
        )
        fig_cat.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_cat, use_container_width=True)