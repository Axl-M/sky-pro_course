# # Сперва импорттируем класс блюпринта
# from flask import Blueprint
#
# # Затем создаем новый блюпринт, выбираем для него имя
# profile_blueprint = Blueprint('profile_blueprint', __name__)
#
# # Создаем вьюшку, используя в декораторе блюпринт вместо арр
# @profile_blueprint.route('/profile/<int:user_id>')
# def profile_page(user_id: int):
#     return f'Я страничкв профиля пользователя {user_id}'