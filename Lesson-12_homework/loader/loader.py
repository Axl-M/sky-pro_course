import logging

from flask import Blueprint, request, render_template
# запуск приложения будет из app (находится на одном уровне с function)
# все будет ок, несмотря на то что здесь function не видит.
from functions import load_posts, uploads_posts


loader_blueprint = Blueprint('loader', __name__, url_prefix='/post', static_folder='static', template_folder='templates')

@loader_blueprint.route('/form/')
def main():
    return render_template('post_form.html')


@loader_blueprint.route('/upload/', methods=['POST'])
# @loader_blueprint.route('/upload/')
def upload():
    try:
        file = request.files['picture']
        filename = file.filename
        if filename.split('.')[-1].lower() not in ['gif', 'png', 'jpg', 'jpeg', 'bmp']:
            logging.info(f'Файл "{filename}" не является изображением')
            return "<h1> Файл не является изображением</h1>"
        content = request.values['content']
        posts = load_posts()
        posts.append({
            'pic': f'/uploads/images/{filename}',
            'content': content
        })
        uploads_posts(posts)
        file.save(f'uploads/images/{filename}')
    except FileNotFoundError:
        logging.error(f'Ошибка при загрузке файла {filename}')
        return "<h1> Файл не найден</h1>"
    else:
        return render_template('post_uploaded.html', pic=f'/uploads/images/{filename}', content=content)