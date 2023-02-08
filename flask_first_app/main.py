from flask import Flask, render_template, request
import utils
from config import path

app = Flask(__name__)

data = utils.load_candidates_from_json(path)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/all_candidates')
def all_candidates():
    """
    Выводит инфо по всем кандидатам
    :return: всё инфо
    """
    return render_template('all_candidates.html', candidates=data)


@app.route('/candidates/<int:id>')
def page_profile(id):
    """
    выводит инфо по конкретному кандидату
    :param id: id кандидата
    :return: инфо о кандидате
    """
    return render_template('single.html', candidate=utils.get_candidate(id))

@app.route('/search/<name>')
def search_candidate_name(name):
    """
    поиск по имени
    :param name:
    :return:
    """
    if name == '':
        return 'Необходимо указать имя'
    candidates = utils.get_candidates_by_name(name)
    return render_template('search.html', candidates=candidates, candidates_len=len(candidates))

@app.route('/skill/', methods=['GET'])
@app.route('/skill/<skill>', methods=['GET'])
def search_candidate_by_skill(skill=None):
    """
    Поиск по скилу
    :param skill:
    :return:
    """
    candidates = utils.get_candidates_by_skill(skill)
    return render_template('skill.html',  candidates=candidates, candidates_len=len(candidates), skill=skill)


if __name__ == '__main__':
    app.run(debug=True)


