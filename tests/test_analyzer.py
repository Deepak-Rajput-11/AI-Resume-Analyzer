from ml.analyzer import analyze_resume

resume_path = "Main_Resume.pdf"

jd_text = """
Python Developer

Required Skills:
Python, Flask, SQL, Django, Git, Pandas
"""

results = analyze_resume(resume_path, jd_text)

print("Resume Skills:", results["resume_skills"])
print("JD Skills:", results["jd_skills"])
print("Matching Skills:", results["matching_skills"])
print("Missing Skills:", results["missing_skills"])
print("Match Percentage:", results["match_percentage"], "%")
print("Text Similarity:", results["text_similarity"], "%")
