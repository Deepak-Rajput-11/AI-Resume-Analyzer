import tempfile
import os

from flask import Flask, request, render_template
from ml.analyzer import analyze_resume

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    resume = request.files.get("resume")
    jd_text = request.form.get("jd_text")

    if not resume or not jd_text:
        return "Resume and job description are required!", 400

    if not resume.filename:
        return "No file selected!", 400

    if not resume.filename.lower().endswith(".pdf"):
        return "Only PDF files are allowed!", 400

    if not resume.read(1):
        return "Uploaded file is empty!", 400

    resume.seek(0)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        resume.save(temp_file.name)
        resume_path = temp_file.name

    try:
        results = analyze_resume(resume_path, jd_text)
    except Exception:
        return "An error occurred while analyzing the resume.", 500
    finally:
        os.remove(resume_path)

    return results


if __name__ == "__main__":
    app.run(debug=True)
