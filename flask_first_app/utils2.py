# Нужно ли это реализовывать ?
import json
# from typing import Union
# from pprint import pprint
from config import path
from classes.candidates_getter import Candidate


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
