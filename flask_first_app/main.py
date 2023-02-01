from flask import Flask
import json
import utils
from classes.candidates_getter import CandidatesGetter

candidate_getter = CandidatesGetter('candidates.json')

app = Flask(__name__)

candidates = utils.load_candidates()

@app.route('/')
def page_index():
    """
    Выводит инфо по всем кандидатам
    :return: всё инфо
    """
    str_candidates = '<pre>'
    for candidate in candidates.values():
        str_candidates += f'Имя кандидата - {candidate["name"]}\n'
        str_candidates += f'Позиция кандидата - {candidate["position"]}\n'
        str_candidates += f'Навыки - {candidate["skills"]}\n\n'
    str_candidates += '</pre>'
    return str_candidates


@app.route('/candidate/<int:id>')
def page_profile(id):
    """
    выводит инфо по конкретному кандидату
    :param id: id кандидата
    :return: инфо о кандидате
    """
    candidate = candidates[id]
    str_candidates = f'<img src={candidate["picture"]}> </img> <br>'
    str_candidates += f'Имя кандидата - {candidate["name"]} <br>'
    str_candidates += f'Позиция кандидата - {candidate["position"]} <br>'
    str_candidates += f'Навыки - {candidate["skills"]} <br><br>'
    return str_candidates

@app.route('/skill/<skill>')    # параметром автоматически передаетс СТРОКА
def page_skills(skill):
    str_candidates = ''
    for candidate in candidates.values():
        candidate_skills = candidate['skills'].split(', ')
        candidate_skills = [x.lower() for x in candidate_skills]
        if skill.lower() in candidate_skills:
            str_candidates += f'Имя кандидата - {candidate["name"]} <br>'
            str_candidates += f'Позиция кандидата - {candidate["position"]} <br>'
            str_candidates += f'Навыки - {candidate["skills"]} <br><br>'
    return str_candidates
# ШагЗ
# Создайте представление /skill/<x> для поиска по навыкам.
# Выведите тех кандидатов, в списке навыков у которых содержится skill .
# <рге>
# Имя кандидата -
# Позиция кандидата
# Навыки через запятую
# Имя кандидата -
# Позиция кандидата
# Навыки через запятую
# Имя кандидата -
# Позиция кандидата
# Навыки через запятую
# <рге>


if __name__ == '__main__':
    app.run(debug=True)   # запуск сервера. debug - чтобы не перезагружать