from flask import Flask, render_template
import utils

app = Flask(__name__)

path = 'candidates.json'
candidates = utils.load_candidates_from_json(path)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/all_candidates')
def page_index():
    """
    Выводит инфо по всем кандидатам
    :return: всё инфо
    """
    return render_template('all_candidates.html', candidates=candidates)


@app.route('/candidates/<int:id>')
def page_profile(id):
    """
    выводит инфо по конкретному кандидату
    :param id: id кандидата
    :return: инфо о кандидате
    """
    candidate = utils.get_candidate(id)
    # candidate = candidates[id]  # <br> тогда <pre> не нужен
    # str_candidates = f'<img src={candidate["picture"]}> <br>'
    # str_candidates += f'Имя кандидата - {candidate["name"]} <br>'
    # str_candidates += f'Позиция кандидата - {candidate["position"]} <br>'
    # str_candidates += f'Навыки - {candidate["skills"]} <br><br>'
    # return str_candidates
    render_template('single.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def search_candidate_name():
    render_template('search.html')

@app.route('/skill/<skill_name>')
def search_candidate_skill():
    render_template('skill.html')


if __name__ == '__main__':
    app.run(debug=True)