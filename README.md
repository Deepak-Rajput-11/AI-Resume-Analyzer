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

### Upcoming Development

- Resume and job description analysis.
- NLP-based text processing.
- Resume-to-job matching.
- Matching score calculation.
- Frontend development.
- Testing and deployment.

## Project Status

The initial setup is complete, and PDF text extraction and basic text preprocessing have been implemented. Resume analysis and matching functionality are currently under development.
