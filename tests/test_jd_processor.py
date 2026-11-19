from ml.jd_processor import process_job_description

jd_text = """
Python Developer

Required Skills:
Python, Flask, SQL, REST APIs

Experience:
0–2 years
"""

cleaned_jd = process_job_description(jd_text)

print(cleaned_jd)
