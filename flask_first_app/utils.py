import json
# from typing import Union
# from pprint import pprint
from config import path
from classes.candidates_getter import Candidate

__data = []
def load_candidates_from_json(path: str) -> dict:
    """
    Возвращает список всех кандидатов
    :param path:
    :return:
    """
    global __data
    with open(path, encoding='utf8') as file:
        __data = json.load(file)
        # print(data)
        # словарь (ключ - порядковый номер = значение id,
        # значение - подсловарь/инфо о кандидате)
        # чтобы потом получать конкретного кандидата по id (ключ)
        # candidates = {}
        # for i in data:
        #     candidates[i['id']] = i
            # print(candidates[i['id']])
        # pprint(candidates)
        # print(data)
    # return candidates
    return __data


def build_candidate_instances_and_skill_list(data: dict) -> tuple[dict, list]:
    """
    Object instance initializer (class Candidate)
    :param data: dictionary of candidates
    :return: list of objects and list of skiills
    """
    candidate_dict = {}
    skill_list = []

    for candidate_id, candidate_data in data.items():
        candidate = Candidate(candidate_id=candidate_id, name=candidate_data['name'], avatar=candidate_data['picture'],
                              position=candidate_data['position'], gender=candidate_data['gender'],
                              age=candidate_data['age'], skills=candidate_data['skills'])
        skill_list.extend([skill.lower() for skill in candidate.skills.split(', ')])
        candidate_dict[candidate_id] = candidate

    skill_list = list(set(skill_list))
    return candidate_dict, skill_list

def get_candidate(candidate_id: int):
    """
    Возвращает одного кандидата по его id
    candidate_dict: Все кандидаты в словаре
    :param candidate_id:
    :return: Экземпляр Candidate
    """
    # for i in candidate_dict:
    #     if candidate_id == i:
    #         return candidate_dict[candidate_id]
    for candidate in __data:
        if candidate['id'] == candidate_id:
            # print(candidate)
            return candidate

    candidate = {'not_found': 'Данные не найдены'}
    return candidate

def get_candidates_by_name(candidate_name: str) -> list[Candidate] | str:
    """
    Возвращает кандидатов по имени
    :candidates: список всех кандидатов
    :param candidate_name:
    :return:
    """
    if candidate_name == '':
        return 'Данные для поиска не указаны'

    return [candidate for candidate in __data if candidate_name.lower() in candidate['name'].lower() ]
    # candidate_list = []
    # # print(candidates.values())
    # for candidate in candidates.values():
    #     if candidate_name  == candidate['name']:
    #         candidate_list.append(candidate)
    #     else:
    #         continue

    # if len(candidate_list) == 0:
    #     return 'По данному запросу ничего не найдено.'

    # return candidate_list


def get_candidates_by_skill(skill_for_search: str) -> list[Candidate] | str:
    """
    Возвращает кандидатов по навыку
    :param skill_for_search:
    :return:
    """
    candidates_list = []

    if skill_for_search == '':
        return 'Данные для поиска не указаны'

    for candidate in __data:
        skills = candidate['skills'].lower().split(', ')
        # for skill in skills:
        if skill_for_search.lower() in skills:
            candidates_list.append(candidate)


    # for candidate in candidates.values():
    #     candidate_skills = candidate['skills'].split(', ')
    #     candidate_skills = [x.lower() for x in candidate_skills]
    #     if skill_for_search.lower() in candidate_skills:
    #         candidates_list.append(candidate)
    return candidates_list

# test
# print(load_candidates_from_json(path))
# candidates = load_candidates_from_json(path)
# print(candidates)
# print(get_candidates_by_name(candidates, "Наташа Приз"))
# print(get_candidate(6))
# print(get_candidates_by_skill(candidates, 'golang'))