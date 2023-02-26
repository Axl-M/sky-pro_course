from flask import Flask, render_template
from candidates_dao import CandidatesDAO
from config import Config

app = Flask(__name__)

# глобальный объект конфигурации Flask
# можете положить свои константы
# print(app.config)
# app.config.from_pyfile('config.py')
# импорт из класса
app.config.from_object(Config)
path = app.config.get('PATH')
print(path)

candidates_dao = CandidatesDAO()

@app.route("/")
def page_index():
    title = app.config.get('PROJECT_NAME')
    description = app.config.get("PROJECT_DESCRIPTION")
    candidates = candidates_dao.get_all()
    return render_template("index.html", candidates=candidates, title=title, description=description)

@app. route("/skill/<skillname>")
def page_skill(skillname):
    candidates = candidates_dao.get_by_skill(skillname)
    return render_template("skill.html", candidates=candidates)

@app.route("/candidate/<int:uid>")
def page_candidate(uid):
    candidate = candidates_dao.get_by_id(uid)
    return render_template("candidate.html", candidate=candidate)


if __name__ == '__main__':
     app.run(debug=True)

