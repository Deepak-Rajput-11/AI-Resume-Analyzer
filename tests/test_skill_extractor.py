from ml.skill_extractor import extract_skills
from ml.skills import SKILLS

text = """
I have experience in Python, Flask, SQL and Pandas.
"""

result = extract_skills(text, SKILLS)

print("Extracted Skills:", result)
