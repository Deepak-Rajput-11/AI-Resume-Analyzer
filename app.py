from flask import Flask, request
from ml.analyzer import analyze_resume

app = Flask(__name__)


@app.route("/")
def home():
    return "AI Resume Analyzer is running!"


@app.route("/analyze", methods=["POST"])
def analyze():
    resume = request.files.get("resume")
    jd_text = request.form.get("jd_text")

    if not resume or not jd_text:
    return "Resume and job description are required!", 400

    results = analyze_resume(resume, jd_text)

    return results


if __name__ == "__main__":
    app.run(debug=True)
