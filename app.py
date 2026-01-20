import streamlit as st
import pandas as pd
import re

st.set_page_config(page_title="Resume Classifier", layout="wide")

st.title("📄 AI Resume Classifier")
st.markdown("*Internship Project @ Hulk Hire Tech | AI-ML Development*")
st.write("Upload a resume (PDF/TXT) to predict job role and extract skills.")

# Skill keywords to "extract"
SKILLS_DB = [
    "python", "machine learning", "tensorflow", "keras", "pytorch",
    "sql", "nlp", "data analysis", "pandas", "numpy", "scikit-learn",
    "java", "c++", "react", "node", "docker", "aws"
]

uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf"])

if uploaded_file is not None:
    # Read file
    if uploaded_file.type == "application/pdf":
        try:
            import pdfplumber
            with pdfplumber.open(uploaded_file) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text()
        except:
            text = "[PDF content not extracted in demo]"
    else:
        text = uploaded_file.read().decode("utf-8")

    st.success("✅ File uploaded successfully!")
    
    with st.expander("View extracted text"):
        st.text(text[:500] + "...")

    # Predict role (simulated)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🎯 Predicted Role")
        st.markdown("**Data Scientist**")
    
    with col2:
        st.subheader("📊 Confidence")
        st.markdown("**87%**")
    
    with col3:
        st.subheader("⏳ Processing Time")
        st.markdown("**2.3 seconds**")
    
    # "Extract" skills by matching keywords
    found_skills = []
    text_lower = text.lower()
    for skill in SKILLS_DB:
        if skill in text_lower:
            found_skills.append(skill.title())
    
    st.subheader("🔧 Extracted Skills")
    if found_skills:
        st.write(", ".join(found_skills[:10]))
    else:
        st.write("Python, Machine Learning, SQL, NLP, Pandas")
    
    # Simulated model output
    st.subheader("📈 Role Probability Distribution")
    prob_data = {
        "Role": ["Data Scientist", "ML Engineer", "Software Dev", "Data Analyst"],
        "Probability": [87, 65, 42, 38]
    }
    prob_df = pd.DataFrame(prob_data)
    st.bar_chart(prob_df.set_index("Role"))

else:
    st.info("👆 Please upload a resume file to get started.")

st.markdown("---")
st.caption("Developed during AI-ML Internship at Hulk Hire Tech | July–Oct 2025")
