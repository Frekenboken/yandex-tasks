from flask import Flask, url_for

app = Flask(__name__)


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion_image')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src='{url_for('static', filename='img/mars.png')}'>
                    <p class="alert alert-primary">Вот она какая, красная планета.<p>
                    <p class="alert alert-secondary">Человечеству мала одна планета.<p>
                    <p class="alert alert-success">Мы сделаем обитаемыми безжизненные пока планеты.<p>
                    <p class="alert alert-danger">И начнем с Марса!<p>
                    <p class="alert alert-warning">Присоединяйся!<p>
                  </body>
                </html>"""


@app.route('/promotion')
def promotion():
    return ("<p>Человечество вырастает из детства.</p>"
            "<p>Человечеству мала одна планета.</p>"
            "<p>Мы сделаем обитаемыми безжизненные пока планеты.</p>"
            "<p>И начнем с Марса!</p>"
            "<p>Присоединяйся!</p>")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
