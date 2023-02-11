# Сперва импорттируем класс блюпринта
from flask import Blueprint, render_template

# Затем создаем новый блюпринт, выбираем для него имя
# было ('profile_blueprint') считаю исправил на правильное
catalog_blueprint = Blueprint('catalog_blueprint', __name__,
                              template_folder='templates')
# Создаем вьюшку, используя в декораторе блюпринт вместо арр
@catalog_blueprint.route('/catalog')
# def profile_page():
def catalog_page():
    # return "Я главная каталога"
    return render_template('main.html')

# Создаем вьюшку, используя в декораторе блюпринт вместо арр
@catalog_blueprint.route('/catalog/<cat>')
# def profilepage(cat):
def category_page(cat):
    # return f'Я ст?раничка каталога категории {cat}'
    return render_template('canegory.html')

@catalog_blueprint.route('/catalog/<cat>/<int:item>')
def item_page(item):
    return render_template('item.html')