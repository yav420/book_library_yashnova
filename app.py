import os
from flask import Flask, render_template
from modules.books import books_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'
app.register_blueprint(books_bp)

if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
    print("\n ССЫЛКИ ДЛЯ ПРОВЕРКИ (Этап 5 - Blueprints):")
    print("   Главная:      http://127.0.0.1:5000/")
    print("   Каталог:      http://127.0.0.1:5000/books")
    print("   Добавить:     http://127.0.0.1:5000/add-book")
@app.route("/")
def index():
    return render_template("index.html")