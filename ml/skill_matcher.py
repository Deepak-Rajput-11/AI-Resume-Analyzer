def compare_skills(resume_skills, jd_skills):
    matching_skills = []
    missing_skills = []

    for skill in jd_skills:
        if skill in resume_skills:
            matching_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matching_skills, missing_skills


def calculate_match_percentage(matching_skills, jd_skills):
    if not jd_skills:
        return 0

    percentage = (len(matching_skills) / len(jd_skills)) * 100

    return round(percentage, 2)
