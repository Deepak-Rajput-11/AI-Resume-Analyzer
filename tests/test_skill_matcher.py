from ml.skill_matcher import compare_skills, calculate_match_percentage

resume_skills = ["Python", "Flask", "SQL", "Pandas"]

jd_skills = ["Python", "Flask", "SQL", "Django", "Git"]

matching, missing = compare_skills(resume_skills, jd_skills)

percentage = calculate_match_percentage(matching, jd_skills)

print("Matching Skills:", matching)
print("Missing Skills:", missing)
print("Skill Match Percentage:", percentage, "%")
