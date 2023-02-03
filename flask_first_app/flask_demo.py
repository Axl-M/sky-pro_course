from flask import Flask

app = Flask('__main__')

@app.route("/")
def home():
    content = """
    <h1>Это моя страничка</h1>
    <p>Страничек много</p>
    <p>Я бог фронтенда</p>
    """
    return content

if __name__ == '__main__':
    app.run()
