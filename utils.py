import json


def load_candidates_from_json(path):
    """
    возвращает список всех кандидатов
    """
    with open(path, 'r', encoding='utf-8') as file:
        file = json.load(file)
        return file


def get_candidate(candidate_id):
    """
    возвращает одного кандидата по его id
    """
    full_candidates = load_candidates_from_json('candidates.json')
    for i in full_candidates:
        if i["id"] == candidate_id:
            return i


def get_candidates_by_name(candidate_name):
    """
    возвращает кандидатов по имени
    """
    candidate_names = []
    full_candidates = load_candidates_from_json('candidates.json')
    for i in full_candidates:
        if candidate_name.lower() in i["name"].lower():
            candidate_names.append(i)
    return candidate_names


def get_candidates_by_skill(skill_name):
    """
    возвращает кандидатов по навыку
    """
    candidate_skills = []
    full_candidates = load_candidates_from_json('candidates.json')
    for i in full_candidates:
        if skill_name.lower() in i["skills"].lower():
            candidate_skills.append(i)
    return candidate_skills
