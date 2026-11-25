from app import app
from io import BytesIO

client = app.test_client()


# Test 1: Missing resume
response = client.post("/analyze", data={"jd_text": "Python developer"})
print("Test 1 - Missing Resume:", response.status_code, response.text)


# Test 2: Missing job description
response = client.post(
    "/analyze", data={"resume": (BytesIO(b"sample pdf"), "resume.pdf")}
)
print("Test 2 - Missing JD:", response.status_code, response.text)


# Test 3: Non-PDF file
response = client.post(
    "/analyze",
    data={
        "resume": (BytesIO(b"sample file"), "resume.txt"),
        "jd_text": "Python developer",
    },
)
print("Test 3 - Non-PDF:", response.status_code, response.text)


# Test 4: Empty file
response = client.post(
    "/analyze",
    data={"resume": (BytesIO(b""), "resume.pdf"), "jd_text": "Python developer"},
)
print("Test 4 - Empty File:", response.status_code, response.text)
