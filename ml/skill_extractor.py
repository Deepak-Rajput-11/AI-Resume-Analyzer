def extract_skills(text, skills):
    found_skills = []

    text = text.lower()

    for skill in skills:
        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills
