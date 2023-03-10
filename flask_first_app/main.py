from flask import Flask, render_template, request, send_from_directory
import utils
from config import path

app = Flask(__name__)
# Ограничиваем размер файла здесь 1Mb
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
# Создаем множество разрешенных расширений
ALLOWED_EXTENSIONS ={'txt', 'pdf', 'png', 'jpg', 'jpeg', 'JPG', 'gif'}

data = utils.load_candidates_from_json(path)

@app.errorhandler(413)
def file_too_large(е):
    return "<h1>Файл большеват</h1><p>Поищите поменьше, плиз!</р>"


@app.errorhandler(404)
def page_not_found(е):
    return "<h1>Упс! Ошибка 404. Страница не найдена.....</h1><p>введите другой адрес</р>"


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

@app.route('/search_form')
def search_form():
    return render_template('form.html')

@app.route('/search/')  # не получаем переменные здесь
def search_page():      # переменные не передаются в функцию
    """
    Поисковый запрос
    наберем прямо в адресной строке:
    /search?s=поищи
    :return:
    """
    # s = request.args['s']       #  данные о запросе мы получаем через объект request.
    s = request.args.get('s')
    if s:
        return f'Вы ввели слово "{s}"'
    return 'Вы ничего не ввели'


@app.route('/filter')
def filter_page():
    """
    в адресе вводим подобное
    /filter?from=10&to=50
    :return:
    """
    from_value = request.args['from']
    to_value = request.args['to']
    return f'Ищем в диапазоне от {from_value} до {to_value}'

@app.route('/todo')
def todo():
    return render_template('todo.html')

@app.route('/add', methods=['POST'])
def add_task():
    # todo_list = {}
    task_name = request.form['task_name']
    # todo_list[len(todo_list) + 1] = task_name
    return render_template('todo.html', task_name=task_name)
    # return f'Добавлена задача: {task_name}'

@app.route('/upload')
def upload_form():
    """
    Эта вьюшка показывает форму, которая отправляет файлы.....
    :return:
    """
    return render_template('upload_file.html')


@app.route('/upload_file', methods=['POST'])
def page_upload_file():
    # Получаем объект картинки из формы
    picture = request.files.get("picture")
    filename = picture.filename
    if filename:                            # если файл был загружен
        extension = filename.split('.')[-1]   # Получаем расширение файла
        # Если расширение файла в белом списке
        if extension in ALLOWED_EXTENSIONS:
            picture.save(f'./uploads/{filename}')
            return f'Файл  "{filename}"  загружен и сохранен'
        else:
            return f'<h2> Tип файлов  "{extension}"  не поддерживается </h2>'
    return 'Файл не был выбран'


# path : _ это модификатор маршрута, такой же как int: или float : он
# позволяет положить в переменную path не один сегмент URL (от одного слеша
# до другого), а сразу весь путь, который написан после uploads
@app.route('/uploads/<path:path>')
def static_dir(path):
    """
        обработает все адреса, которые начинаются с uploads
        :param path:
        :return:
        """
    # send_from_directory(directory, path)
    # функция Flask для передачи клиенту запрошенного фала при указании папки и пути.
    return send_from_directory("uploads", path)

if __name__ == '__main__':
    app.run(debug=True)


