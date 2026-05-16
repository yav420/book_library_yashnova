import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=True)
    description = db.Column(db.Text, nullable=True)
    cover = db.Column(db.String(100), default='placeholder.png')
from modules.books import books_bp
app.register_blueprint(books_bp)
with app.app_context():
    db.create_all()
    print("База данных инициализирована.")
@app.route("/")
def index():
    return render_template("index.html")

if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
    print("\n ССЫЛКИ ДЛЯ ПРОВЕРКИ (Этап 6 - SQLAlchemy):")
    print("   Главная:      http://127.0.0.1:5000/")
    print("   Каталог:      http://127.0.0.1:5000/books")
    print("   Добавить:     http://127.0.0.1:5000/add-book")