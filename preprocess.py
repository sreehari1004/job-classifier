import re

def preprocess_skills(skills_text):
    if not isinstance(skills_text, str):
        return ""
    skills_text = skills_text.lower()
    skills_text = re.sub(r'[^a-zA-Z0-9\s]', '', skills_text)
    skills_text = re.sub(r'\s+', ' ', skills_text).strip()
    return skills_text
