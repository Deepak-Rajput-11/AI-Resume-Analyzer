# AI Resume Analyzer

An NLP and Machine Learning-powered application that analyzes resumes against job descriptions to help candidates understand their relevance to specific job opportunities.

## Overview

AI Resume Analyzer aims to help job seekers evaluate how well their resumes match a particular job description.

The application will extract information from PDF resumes, analyze job requirements, identify matching and missing skills, and provide an overall relevance score with improvement suggestions.

The goal is to go beyond basic keyword matching by exploring both traditional NLP techniques and semantic similarity.

## Planned Features

- Upload resumes in PDF format.
- Extract text and relevant information from resumes.
- Analyze job descriptions.
- Identify matching and missing skills.
- Calculate resume-to-job relevance scores.
- Use NLP and ML techniques for text analysis.
- Generate suggestions for improving resume relevance.

**Note:** These are planned features. They will be implemented progressively during development.

## Technology Stack

| Technology            | Purpose                         |
| --------------------- | ------------------------------- |
| Python                | Core programming language       |
| Flask                 | Backend framework               |
| HTML, CSS, JavaScript | Frontend                        |
| PyMuPDF               | PDF text extraction             |
| Pandas & NumPy        | Data processing                 |
| NLTK                  | NLP and text preprocessing      |
| Scikit-learn          | TF-IDF and traditional ML tools |
| Sentence Transformers | Semantic text embeddings        |
| Pytest                | Testing                         |
| Git & GitHub          | Version control                 |

## Project Architecture

The application is planned around three main components:

1. **Frontend:** Handles resume uploads, job description input and result presentation.
2. **Backend:** Handles requests, file processing and communication between components.
3. **NLP/ML Engine:** Processes resume and job description text and performs matching analysis.

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

**### Day 3 — Skill Extraction & Matching**

- Implemented job description preprocessing.
- Created a keyword-based skill extraction module.
- Created a centralized skill collection for reusable skill detection.
- Implemented skill matching between resume and job description skills.
- Added identification of matching and missing skills.
- Implemented skill match percentage calculation.
- Created and executed tests for skill extraction and skill matching.

**### Day 4 — Analysis Pipeline & Input Validation**

- Created a central analysis module to coordinate existing processing components.
- Integrated resume PDF extraction and text preprocessing.
- Integrated job description processing and skill extraction.
- Implemented combined resume and job description skill analysis.
- Improved skill extraction accuracy using regular expressions and word boundaries.
- Added input validation for missing resume paths, nonexistent PDF files, and empty job descriptions.
- Tested the complete analysis pipeline and validation cases successfully.

### Upcoming Development

- Resume and job description analysis.
- NLP-based text processing.
- Resume-to-job matching.
- Matching score calculation.
- Frontend development.
- Testing and deployment.

**## Project Status**

The initial setup, PDF text extraction, text preprocessing, skill extraction, skill matching, and integrated analysis pipeline have been implemented. Input validation is also in place. Advanced NLP/ML-based resume relevance analysis and frontend development are currently under development.
