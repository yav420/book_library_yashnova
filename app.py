import os
from flask import Flask, request

app = Flask(__name__)
books = [
    {"id": 1, "title": "Война и мир", "author": "Лев Толстой", "genre": "Роман", "year": 1869,
     "description": "Эпопея о русском обществе."},
    {"id": 2, "title": "Преступление и наказание", "author": "Фёдор Достоевский", "genre": "Психологический роман",
     "year": 1866, "description": "История Раскольникова."},
    {"id": 3, "title": "Мастер и Маргарита", "author": "Михаил Булгаков", "genre": "Фантастика", "year": 1967,
     "description": "Визит дьявола в Москву."},
    {"id": 4, "title": "Евгений Онегин", "author": "Александр Пушкин", "genre": "Роман в стихах", "year": 1833,
     "description": "Жизнь лишнего человека."}
]

if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
    print(" ССЫЛКИ ДЛЯ ПРОВЕРКИ (скопируйте или откройте командой):")
    for book in books:
        print(f"   Книга #{book['id']}: http://127.0.0.1:5000/books/{book['id']}")
    print("\n Поиск:")
    print("   http://127.0.0.1:5000/search?q=Толстой")
    print("   http://127.0.0.1:5000/search?q=Достоевский")



@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Библиотека книг</title>
        <link rel="stylesheet" href="/static/css/style.css">
    </head>
    <body>
        <h1>Библиотека книг</h1>
        <img src="/static/images/placeholder.png" alt="Заглушка" width="200">
    </body>
    </html>
    """


@app.route("/books")
def books_list():
    items = "".join(f"<li>{book['title']}</li>" for book in books)
    return f"<!DOCTYPE html><html><body><ol>{items}</ol></body></html>"


@app.route("/books/<int:book_id>")
def book_detail(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        return "Книга не найдена", 404

    return f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>{book['title']}</title>
        <link rel="stylesheet" href="/static/css/style.css">
    </head>
    <body>
        <h1>{book['title']}</h1>
        <p><strong>Автор:</strong> {book['author']}</p>
        <p><strong>Жанр:</strong> {book['genre']}</p>
        <p><strong>Год:</strong> {book['year']}</p>
        <p><strong>Описание:</strong> {book['description']}</p>
        <p><a href="/books">← Назад к списку</a></p>
    </body>
    </html>
    """


@app.route("/search")
def search():
    q = request.args.get("q", "").strip()

    if not q:
        return "Введите поисковый запрос", 400

    results = [
        b for b in books
        if q.lower() in b["title"].lower() or q.lower() in b["author"].lower()
    ]

    if not results:
        return "<p>Ничего не найдено</p>"

    items = "".join(f"<li>{b['title']} ({b['author']})</li>" for b in results)
    return f"<!DOCTYPE html><html><body><ul>{items}</ul></body></html>"