import json
# from typing import Union
# from pprint import pprint
from config import path
from classes.candidates_getter import Candidate

__data = []         # чтобы нельзя было получить данные из внешнего файла
def load_candidates_from_json(path: str) -> dict:
    """
    Возвращает список всех кандидатов
    :param path:
    :return:
    """
    global __data
    with open(path, encoding='utf8') as file:
        __data = json.load(file)
        # словарь (ключ - порядковый номер = значение id,
        # значение - подсловарь/инфо о кандидате)
        # чтобы потом получать конкретного кандидата по id (ключ)
        # __data = {}
        # for i in __data:
        #     __data[i['id']] = i
    return __data


def get_candidate(candidate_id: int):
    """
    Возвращает одного кандидата по его id
    :param candidate_id:
    :return: Экземпляр Candidate
    """
    for candidate in __data:
        if candidate['id'] == candidate_id:
            return candidate

    return {'not_found': 'Данные не найдены'}

def get_candidates_by_name(candidate_name: str) -> list[Candidate] | str:
    """
    Возвращает кандидатов по имени
    :param candidate_name:
    :return:
    """
    if candidate_name == '':
        return 'Данные для поиска не указаны'

    return [candidate for candidate in __data if candidate_name.lower() in candidate['name'].lower() ]


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
        if skill_for_search.lower() in skills:
            candidates_list.append(candidate)

    return candidates_list

