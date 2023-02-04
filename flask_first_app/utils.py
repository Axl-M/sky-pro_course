import json
# from pprint import pprint

path = 'candidates.json'
def load_candidates_from_json(path):
    """
    Возвращает список всех кандидатов
    :param path:
    :return:
    """
    with open(path, encoding='utf8') as file:
        data = json.load(file)
        # print(data)
        # словарь (ключ - порядковый номер = значение id,
        # значение - подсловарь/инфо о кандидате)
        # чтобы потом получать конкретного кандидата по id (ключ)
        candidates = {}
        for i in data:
            candidates[i['id']] = i
            # print(candidates[i['id']])
        # pprint(candidates)
        # print(data)
        return candidates

def get_candidate(candidate_id):
    """
    Возвращает одного кандидата по его id
    :param candidate_id:
    :return:
    """
    return candidates[candidate_id]

def get_candidates_by_name(candidates, candidate_name):
    """
    Возвращает кандидатов по имени
    :candidates: список всех кандидатов
    :param candidate_name:
    :return:
    """
    if candidate_name == '':
        return 'Данные для поиска не указаны'

    candidate_list = []
    # print(candidates.values())
    for candidate in candidates.values():
        if candidate_name  == candidate['name']:
            candidate_list.append(candidate)
        else:
            continue

    return candidate_list


def get_candidates_by_skill(skill):
    """
    Возвращает кандидатов по навыку
    :param skill:
    :return:
    """
    candidates_list = []
    for candidate in candidates.values():
        candidate_skills = candidate['skills'].split(', ')
        candidate_skills = [x.lower() for x in candidate_skills]
        if skill.lower() in candidate_skills:
            candidates_list.append(candidate)
    return candidates_list

# test
# print(load_candidates_from_json(path))
candidates = load_candidates_from_json(path)
# print(candidates)
# print(get_candidates_by_name(candidates, "Наташа Приз"))
# print(get_candidate(6))
print(get_candidates_by_skill('golang'))