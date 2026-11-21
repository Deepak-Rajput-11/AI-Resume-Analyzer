from ml.text_similarity import calculate_text_similarity

resume_text = """
I am a Python developer with experience in Flask,
SQL and backend development.
"""

jd_text = """
Looking for a Python developer with Flask,
SQL and backend development skills.
"""

score = calculate_text_similarity(resume_text, jd_text)

print("Text Similarity:", score, "%")
