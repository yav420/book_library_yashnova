from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <link rel="stylesheet" href="/static/css/style.css">
    </head>
    <body>
        <h1>Библиотека книг</h1>
        <img src="/static/images/placeholder.png" alt="Заглушка" style="max-width: 300px; height: auto;">
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)