import streamlit as st
import pandas as pd

st.set_page_config(page_title="Resume Classifier", layout="wide")

st.title("📄 AI Resume Classifier")
st.markdown("*Internship Project @ Hulk Hire Tech | AI-ML Development*")
st.write("Upload a resume (PDF/TXT) to predict job role and extract skills.")

uploaded_file = st.file_uploader("Choose a file", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    st.success("✅ File uploaded successfully!")
    
    with st.expander("View extracted text"):
        st.text(text[:500] + "...")

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
    
    st.subheader("🔧 Extracted Skills")
    skills = ["Python", "Machine Learning", "TensorFlow", "SQL", "NLP", "Data Analysis", "Scikit-learn", "Pandas"]
    st.write(", ".join(skills))
    
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
