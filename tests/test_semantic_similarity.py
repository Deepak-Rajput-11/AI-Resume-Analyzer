from ml.semantic_similarity import calculate_semantic_similarity

resume_text = """
I developed web applications using Python and Flask.
I have experience building backend systems and REST APIs.
"""

jd_text = """
Looking for a developer who can build software applications
using Python and Flask, with backend development experience.
"""

score = calculate_semantic_similarity(resume_text, jd_text)

print("Semantic Similarity:", score, "%")
