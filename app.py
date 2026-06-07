from utils import extract_text

job_description = """
python
sql
machine learning
data analysis
communication
"""

resume_text = extract_text("sample_resume.pdf")

keywords = job_description.lower().split()

matched_keywords = []

for keyword in keywords:
    if keyword in resume_text.lower():
        matched_keywords.append(keyword)

ats_score = (len(matched_keywords) / len(keywords)) * 100

print(f"ATS Score: {ats_score:.2f}%")
print("\nMatched Keywords:")

for keyword in matched_keywords:
    print(f"- {keyword}")