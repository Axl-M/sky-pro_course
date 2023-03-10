from flask import Blueprint, render_template
from .dao.vacancies_dao import VacanciesDAO

vacancies_blueprint = Blueprint('vacancies_blueprint', __name__, template_folder='templates')

# Создаем DAO для вакансий
vacancies_dao = VacanciesDAO('../data/vacancies.json')

@vacancies_blueprint.route('/vacancies')
def page_vacancies():
    vacancies = vacancies_dao.get_all()
    return render_template('vacancies_index.htm', vacancies=vacancies)

@vacancies_blueprint.route('/vacancies/<int:pk>')
def page_vacancy(pk):
    vacancy = vacancies_dao.get_by_pk(1)
    return render_template('vacancies_single.html', vacancy=vacancy)
