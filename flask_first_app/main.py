from flask import Flask
import json
import utils
from classes.candidates_getter import CandidatesGetter

candidate_getter = CandidatesGetter('candidates.json')

app = Flask(__name__)

candidates = utils.load_candidates()

# assert(False)   # остановка выполнения программы

@app.route('/')
def page_index():
    """
    Выводит инфо по всем кандидатам
    :return: всё инфо
    """
    str_candidates = '<pre>'    # <pre> чтобы \n корректно отрабатывались
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
    candidate = candidates[id]  # <br> тогда <pre> не нужен
    str_candidates = f'<img src={candidate["picture"]}> <br>'
    str_candidates += f'Имя кандидата - {candidate["name"]} <br>'
    str_candidates += f'Позиция кандидата - {candidate["position"]} <br>'
    str_candidates += f'Навыки - {candidate["skills"]} <br><br>'
    return str_candidates

@app.route('/skill/<skill>')    # параметром автоматически передается СТРОКА
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



if __name__ == '__main__':
    app.run(debug=True)   # запуск сервера. debug - чтобы не перезагружать