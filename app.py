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
    
    jd_words = job_description.lower().split()

    matched = []

    resume_name = uploaded_file.name.lower()

    for word in jd_words:
        if word in resume_name:
            matched.append(word)

    score = min(len(matched) * 10, 100)

    st.metric("ATS Score", f"{score}%")

    st.subheader("Matched Keywords")

    if matched:
        for keyword in matched:
            st.write(f"✅ {keyword}")
    else:
        st.write("No matching keywords found")