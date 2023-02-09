# import logging
# from flask import Flask, request
#
# logging.basicConfig(filename="basic.log")
# # сообщени теперь отправляются в журнал, а не в консоль
#
# app = Flask(__name__)
# @app.route('/')
# def page_index():
#     return "Главная страница"
# @app.route('/store')
# def page_store():
#     return "Страница магазина"
# @app.route('/store/<cat>')
# def pagecat(cat):
#     return f'Страница категории {cat} '
#
#
# app.run()

import logging
from flask import Flask
    # request, rendertemplate

logging.basicConfig(filename="basic.log", level=logging.INFO)

app = Flask(__name__)
@app.route('/')
def page_index():
    logging.info("Главная страница запрошена")
    return "Главная страница"
@app.route('/store')
def page_store():
    logging.info("Страница магазина запрошена")
    return "Страница магазина "
@app.route('/store/<cat>')
def pagecat(cat):
    logging.info(f'Страница категории {cat} запрошена')
    return f'Страница категории {cat} '

app.run()

# Уровень события Как вызывается      Что означает
# DEBUG       logging.debug(...)      Отладочные записи (покажется всё)
# INFO        logging.info()          Записи о штатной работе (покажется всё, начиная с INFO)
# WARNING     logging.warning(...)    Записи о нарушениях в работе
# ERROR       logging.error(...)      Записи о поломке в приложении
# CRITICAL    logging.critical(...)   Записи о критической неисправности
# EXCEPTION   logging.exception(...)  Записи, которые делают обработчики ошибок





