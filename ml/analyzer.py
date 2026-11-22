from pathlib import Path
from ml.pdf_extractor import extract_text_from_pdf
from ml.text_preprocessor import clean_text
from ml.jd_processor import process_job_description
from ml.skill_extractor import extract_skills
from ml.skills import SKILLS
from ml.skill_matcher import compare_skills, calculate_match_percentage
from ml.text_similarity import calculate_text_similarity
from ml.semantic_similarity import calculate_semantic_similarity


def analyze_resume(resume_pdf_path, jd_text):

    if not resume_pdf_path:
        raise ValueError("Resume PDF path is required.")

    if not Path(resume_pdf_path).is_file():
        raise FileNotFoundError("Resume PDF file was not found.")

    if not jd_text or not jd_text.strip():
        raise ValueError("Job description cannot be empty.")

    # Extract and clean resume text
    resume_text = extract_text_from_pdf(resume_pdf_path)
    cleaned_resume = clean_text(resume_text)

    # Process job description
    cleaned_jd = process_job_description(jd_text)

    # Calculate text similarity
    text_similarity = calculate_text_similarity(cleaned_resume, cleaned_jd)

    # Calculate semantic similarity
    semantic_similarity = calculate_semantic_similarity(cleaned_resume, cleaned_jd)

    # Extract skills from both inputs
    resume_skills = extract_skills(cleaned_resume, SKILLS)
    jd_skills = extract_skills(cleaned_jd, SKILLS)

    # Compare skills
    matching_skills, missing_skills = compare_skills(resume_skills, jd_skills)

    # Calculate match percentage
    match_percentage = calculate_match_percentage(matching_skills, jd_skills)

    return {
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
        "match_percentage": match_percentage,
        "text_similarity": text_similarity,
        "semantic_similarity": semantic_similarity,
    }
