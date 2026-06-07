import streamlit as st
from utils import extract_text
import tempfile

st.title("Resume ATS Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze Resume"):

    if uploaded_file is not None and job_description:

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            pdf_path = tmp_file.name

        resume_text = extract_text(pdf_path).lower()

        keywords = job_description.lower().split()

        matched_keywords = []

        for keyword in keywords:
            if keyword in resume_text:
                matched_keywords.append(keyword)

        ats_score = (len(matched_keywords) / len(keywords)) * 100

        st.metric("ATS Score", f"{ats_score:.2f}%")

        st.subheader("Matched Keywords")

        if matched_keywords:
            for keyword in matched_keywords:
                st.write(f"✅ {keyword}")
        else:
            st.write("No matching keywords found")