from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    content = """
    <h1>Это моя страничка</h1>
    <p>Страничек много</p>
    <p>Я бог фронтенда</p>
    <hr>
    <br>
    /form/  
    """
    return content

@app.route("/form/")
def form():
    return render_template('/my_form.html', name='Александр')

if __name__ == '__main__':
    app.run()
