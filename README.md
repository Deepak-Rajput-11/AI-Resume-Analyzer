# AI Resume Analyzer

An NLP and Machine Learning-powered application that analyzes resumes against job descriptions to help candidates understand their relevance to specific job opportunities.

## Overview

AI Resume Analyzer aims to help job seekers evaluate how well their resumes match a particular job description.

The application extracts text from PDF resumes, processes job requirements, identifies matching and missing skills, and calculates resume-to-job relevance scores.

The project combines traditional NLP techniques and semantic similarity to go beyond basic keyword matching.

## Planned Features

- Upload resumes in PDF format.
- Extract text from resumes.
- Process and analyze job descriptions.
- Identify matching and missing skills.
- Calculate resume-to-job relevance scores.
- Use NLP and ML techniques for text similarity analysis.
- Generate suggestions for improving resume relevance.
- Present analysis results through a user-friendly interface.

**Note:** Features are being implemented progressively during development.

## Technology Stack

| Technology            | Purpose                                    |
| --------------------- | ------------------------------------------ |
| Python                | Core programming language                  |
| Flask                 | Backend framework                          |
| HTML, CSS, JavaScript | Frontend development                       |
| PyMuPDF               | PDF text extraction                        |
| Scikit-learn          | TF-IDF vectorization and cosine similarity |
| Sentence Transformers | Semantic embeddings and similarity         |
| Pytest                | Testing                                    |
| Git & GitHub          | Version control                            |

## Project Architecture

The application is organized around three main components:

1. **Frontend:** Handles resume uploads, job description input, and result presentation.
2. **Backend:** Handles application requests, file processing, and communication between components.
3. **NLP/ML Engine:** Processes resume and job description text and performs matching and similarity analysis.

## Development Progress

### Day 1 — Initial Setup

- Defined project architecture and technology stack.
- Created and activated a Python virtual environment.
- Installed Flask.
- Created the initial Flask application.
- Tested the application using a local development server.
- Created the initial project folder structure.
- Added `requirements.txt` and `.gitignore`.
- Initialized Git and connected the project to GitHub.
- Created the initial Git commit and pushed it to GitHub.
- Created the initial project README.

### Day 2 — PDF Extraction & Text Preprocessing

- Installed PyMuPDF for PDF text extraction.
- Implemented PDF text extraction using PyMuPDF.
- Added support for extracting text from multiple pages.
- Created a text preprocessing module.
- Implemented whitespace normalization to clean extracted text.
- Tested the extraction and preprocessing pipeline using a sample resume.

### Day 3 — Skill Extraction & Matching

- Implemented job description preprocessing.
- Created a keyword-based skill extraction module.
- Created a centralized skill collection for reusable skill detection.
- Implemented skill matching between resume and job description skills.
- Added identification of matching and missing skills.
- Implemented skill match percentage calculation.
- Created and executed tests for skill extraction and skill matching.

### Day 4 — Analysis Pipeline & Input Validation

- Created a central analysis module to coordinate existing processing components.
- Integrated resume PDF extraction and text preprocessing.
- Integrated job description processing and skill extraction.
- Implemented combined resume and job description skill analysis.
- Improved skill extraction accuracy using regular expressions and word boundaries.
- Added input validation for missing resume paths, nonexistent PDF files, and empty job descriptions.
- Tested the complete analysis pipeline and validation cases successfully.

### Day 5 — TF-IDF & Text Similarity

- Installed Scikit-learn for NLP-based text similarity analysis.
- Implemented TF-IDF vectorization to convert resume and job description text into numerical representations.
- Implemented cosine similarity to measure textual similarity between documents.
- Created a dedicated text similarity module.
- Integrated text similarity calculation into the central resume analysis pipeline.
- Tested the complete analyzer with both skill matching and text similarity calculations.

### Day 6 — Semantic Similarity with Sentence Transformers

- Installed Sentence Transformers for semantic text analysis.
- Explored sentence embeddings and their role in understanding textual meaning.
- Integrated the pretrained `all-MiniLM-L6-v2` model.
- Implemented semantic similarity using sentence embeddings and cosine similarity.
- Created a dedicated semantic similarity module.
- Integrated semantic similarity into the central resume analysis pipeline.
- Tested the complete analyzer with skill matching, TF-IDF similarity, and semantic similarity.

### Day 7 — Flask Backend & Request Handling

- Reviewed the existing Flask application structure.
- Explored Flask routes and HTTP POST requests.
- Created an `/analyze` POST route to receive resume uploads and job description text.
- Used Flask's `request.files` to retrieve uploaded resume files.
- Used Flask's `request.form` to retrieve job description input.
- Introduced the connection between Flask routes and the central resume analyzer.

### Day 8 — Flask Backend Integration

- Implemented temporary PDF file handling for uploaded resumes.
- Connected the Flask `/analyze` POST route to the central `analyze_resume()` function.
- Integrated resume upload and job description input handling.
- Implemented temporary file cleanup after analysis.
- Returned analysis results as JSON responses.
- Installed Requests for backend route testing.
- Created a Flask route test to submit PDF resumes and job descriptions.
- Successfully tested the complete Flask-to-analyzer workflow.

### Day 9 — Backend Validation & Error Handling

- Added validation for missing resume and job description inputs.
- Implemented uploaded filename validation.
- Restricted resume uploads to PDF file extensions.
- Added empty-file validation.
- Implemented exception handling for unexpected resume analysis errors.
- Ensured temporary uploaded files are cleaned up after analysis.
- Created and executed tests for invalid backend inputs using Flask's test client.
- Successfully tested missing resume, missing job description, non-PDF uploads, and empty files.

## Upcoming Development

- Develop the Flask backend functionality for resume uploads and job description input.
- Build the frontend interface.
- Display resume analysis results.
- Generate resume improvement suggestions.
- Perform application testing and debugging.
- Deploy the application.

## Project Status

The project currently supports PDF text extraction, text preprocessing, keyword-based skill extraction, skill matching, input validation, TF-IDF-based text similarity, and semantic similarity using Sentence Transformers.

The central analysis pipeline integrates these components and has been tested successfully. Backend application functionality, frontend development, and deployment are the next stages of development.
