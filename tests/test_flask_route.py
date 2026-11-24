import requests

url = "http://127.0.0.1:5000/analyze"

resume_path = "Main_Resume.pdf"

jd_text = """
Python Developer

Required Skills:
Python, SQL, Flask, Git, Pandas
"""

with open(resume_path, "rb") as resume:
    files = {"resume": resume}

    data = {"jd_text": jd_text}

    response = requests.post(url, files=files, data=data)

print("Status Code:", response.status_code)
print("Analysis Results:", response.text)
