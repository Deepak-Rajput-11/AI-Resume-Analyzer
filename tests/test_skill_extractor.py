from ml.skill_extractor import extract_skills

text = """
I work with Python, Flask, SQL and C++.
I also have experience with NoSQL databases.
"""

skills = ["Python", "Flask", "SQL", "C++", "C"]

result = extract_skills(text, skills)

print("Extracted Skills:", result)
