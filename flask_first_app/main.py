from flask import Flask
import json
import utils
from classes.candidates_getter import CandidatesGetter

candidate_getter = CandidatesGetter('candidates.json')

app = Flask(__name__)

candidates = utils.load_candidates()

@app.route('/')
def page_index():
    # candidates = candidate_getter.get_all()
    str_candidates = '<pre>'
    for candidate in candidates.values():
        str_candidates += f'Имя кандидата - {candidate["name"]}\n'
        str_candidates += f'Позиция кандидата - {candidate["position"]}\n'
        str_candidates += f'Навыки - {candidate["skills"]}\n\n'
    str_candidates += '</pre>'
    return str_candidates


@app.route('/candidate/<int:id>')
def page_profile(id):
    candidate = candidates[id]
    # str_candidates = f'< img src = "https://picsum.photos/200"> \n'
    str_candidates = f'<img src={candidate["picture"]}> </img> <br>'
    # str_candidates += f'{candidate["picture"]} \n'
    str_candidates += '<pre>'
    str_candidates += f'Имя кандидата - {candidate["name"]} <br>'
    str_candidates += f'Позиция кандидата - {candidate["position"]} <br>'
    str_candidates += f'Навыки - {candidate["skills"]} <br><br>'
    str_candidates += '</pre>'
    return str_candidates

# app.add_url_rule('/', view_func=page_index)

#
# Шаг 2
# Создайте представление для роута candidate/<x> ,
# Который бы выводил данные про кандидата так:
# <img src="(ссылка на картинку)">
# <рге>
# Имя кандидата -
# Позиция кандидата
# Навыки через запятую
# </рге>

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