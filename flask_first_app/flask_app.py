from flask import Flask

app = Flask(__name__)

@app.route('/')  # так гораздо элегантнее
def page_index():
    return '<pre> Я страничка  :) \n            и я главна страничка!  \n ещё адреса' \
           '\n /feed' \
           '\n /profile ' \
           '\n /messages ' \
           '\n /users/НОМЕР ' \
           '\n /catalog/НАИМЕНОВАНИЕ_ТОВАРА  </pre>'

# app.add_url_rule('/', view_func=page_index)

@app.route('/profile')
def page_profile():
    return 'Страница профиля пользователя'

@app.route('/feed/')
def page_feed():
    return 'Лента пользователя'

@app.route('/messages')
def page_messages():
    return 'Новых сообщений нет'

@app.route('/users/<uid>')
def profile(uid):
    return f'<h1> Профиль {uid} </h1>'

@app.route('/catalog/<itemid>')
def tovar(itemid):
    return f'<h1> Страничка товара {itemid}</h1>'


app.run()   # запуск сервера