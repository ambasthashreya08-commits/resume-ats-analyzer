import streamlit as st

st.title("Resume ATS Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze Resume"):
    st.success("Resume analysis feature coming next")