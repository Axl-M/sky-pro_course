# Сперва импорттируем класс блюпринта
from flask import Blueprint

# Затем создаем новый блюпринт, выбираем для него имя
catalog_blueprint = Blueprint('profile_blueprint', __name__)
# Создаем вьюшку, используя в декораторе блюпринт вместо арр
@catalog_blueprint.route('/catalog')
def profile_page():
    return "Я главная каталога"

# Создаем вьюшку, используя в декораторе блюпринт вместо арр
@catalog_blueprint.route('/catalog/<cat>')
def profilepage(cat):
    return f'Я страничка каталога категории {cat}'