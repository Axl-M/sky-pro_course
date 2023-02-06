from flask import Flask, render_template, request
import utils
from config import path

app = Flask(__name__)

data = utils.load_candidates_from_json(path)

# candidate_dict, skill_list = utils.build_candidate_instances_and_skill_list(candidates)

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
    # candidate = utils.get_candidate(id)
    # candidate = candidates[id]  # <br> тогда <pre> не нужен
    # str_candidates = f'<img src={candidate["picture"]}> <br>'
    # str_candidates += f'Имя кандидата - {candidate["name"]} <br>'
    # str_candidates += f'Позиция кандидата - {candidate["position"]} <br>'
    # str_candidates += f'Навыки - {candidate["skills"]} <br><br>'
    # return str_candidates
    # render_template('single.html', candidate=candidate)
    return render_template('single.html', candidate=utils.get_candidate(id))
    # return utils.get_candidate(id)

# print(utils.get_candidate(6))

@app.route('/search/<name>')
def search_candidate_name(name):
    if name == '':
        return 'Необходимо указать имя'
    candidates = utils.get_candidates_by_name(name)
    return render_template('search.html', candidates=candidates, candidates_len=len(candidates))
    # return utils.get_candidates_by_name(name)


# @app.route('/search_by_skill', method=['GET', 'POST'])
# def page_search_by_skill():
#     if request.method == 'POST':
#         search_data = request.form.get('search_data_from_input').lower()
#         return render_template('search_by_skill.html', search_data=get_candidates_by_skill(candidate_dict, search_data))
#     return render_template('search_by_skill.html')

# @app.route('/skill/', methods=['GET'])
@app.route('/skill/<skill>', methods=['GET'])
def search_candidate_by_skill(skill=None):
    candidates = utils.get_candidates_by_skill(skill)
    print(candidates)
    # render_template('skill.html', skill=skill, skill_list=skill_list,
    #                 search_data=get_candidate_by_skill(candidate_dict, skill))
    return render_template('skill.html',  candidates=candidates, candidates_len=len(candidates), skill=skill)

if __name__ == '__main__':
    app.run(debug=True)


