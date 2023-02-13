from flask import Blueprint, request, render_template
# запуск приложения будет из app (находится на одном уровне с function)
# все будет ок, несмотря на то что здесь function не видит.
from functions import load_posts


loader_blueprint = Blueprint('loader', __name__, url_prefix='/post', static_folder='static', template_folder='templates')

@loader_blueprint.route('/form/')
def main():
    return render_template('post_form.html')


# @main_blueprint.route('/search/')
# def search():
#     search_by = request.args['s']
#     posts = [x for x in load_posts() if search_by.lower() in x['content'].lower()]
#     return render_template('post_list.html', search_by=search_by, posts=posts)