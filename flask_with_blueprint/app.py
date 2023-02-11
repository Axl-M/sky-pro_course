from flask import Flask, render_template

# Импортируем блюпринты из их пакетов
from catalog.views import catalog_blueprint
from profiles.views import profile_blueprint
# Импортируем блюпринты из их пакетов
from messages.views import messages_blueprint

app = Flask(__name__)

# Регистрируем первый блюпринт
app.register_blueprint(catalog_blueprint)
# И второй тоже регистрируем
app.register_blueprint(profile_blueprint)
# Регистрируем блюпринт с указание префикса
app.register_blueprint(messages_blueprint, url_prefix='/messages')

app.run()
