import json
from pprint import pprint

def load_candidates():
    with open('candidates.json', encoding='utf8') as file:
        data = json.load(file)
        print(data)
        # словарь (ключь - порядковый номер = id, значение - подсловарь/инфо о кандидате)
        candidates = {}
        for i in data:
            candidates[i['id']] = i
            # print(candidates[i['id']])
        # pprint(candidates)
        # print(data)
        return candidates

load_candidates()
