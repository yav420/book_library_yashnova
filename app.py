import os
from flask import Flask, request, render_template, abort, flash, redirect, url_for
from forms import BookForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'
books = [
    {"id": 1, "title": "Война и мир", "author": "Лев Толстой", "genre": "Роман", "year": 1869,
     "description": "Эпопея о русском обществе.", "cover": "placeholder.png"},
    {"id": 2, "title": "Преступление и наказание", "author": "Фёдор Достоевский", "genre": "Психологический роман",
     "year": 1866, "description": "История Раскольникова.", "cover": "placeholder.png"},
    {"id": 3, "title": "Мастер и Маргарита", "author": "Михаил Булгаков", "genre": "Фантастика", "year": 1967,
     "description": "Визит дьявола в Москву.", "cover": "placeholder.png"},
    {"id": 4, "title": "Евгений Онегин", "author": "Александр Пушкин", "genre": "Роман в стихах", "year": 1833,
     "description": "Жизнь лишнего человека.", "cover": "placeholder.png"}
]

if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
    print("\n ССЫЛКИ ДЛЯ ПРОВЕРКИ (Этап 2 - Jinja2):")
    for book in books:
        print(f"   Книга #{book['id']}: http://127.0.0.1:5000/books/{book['id']}")
    print("\n Поиск:")
    print("   http://127.0.0.1:5000/search?q=Толстой")
    print("   http://127.0.0.1:5000/search?q=Достоевский")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/books")
def books_list():
    return render_template("books_list.html", books=books)


@app.route("/books/<int:book_id>")
def book_detail(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        abort(404)
    return render_template("book_detail.html", book=book)


@app.route("/search")
def search():
    q = request.args.get("q", "").strip()

    if not q:
        return render_template("search.html", q=None, results=None)

    results = [
        b for b in books
        if q.lower() in b["title"].lower() or q.lower() in b["author"].lower()
    ]
    return render_template("search.html", q=q, results=results)

@app.route("/add-book", methods=["GET", "POST"])
def add_book():
    form = BookForm()

    if form.validate_on_submit():
        # Генерируем новый ID
        new_id = max(b["id"] for b in books) + 1 if books else 1

        new_book = {
            "id": new_id,
            "title": form.title.data,
            "author": form.author.data,
            "genre": form.genre.data,
            "year": form.year.data,
            "description": form.description.data,
            "cover": form.cover_filename.data or "placeholder.png"  # Placeholder по умолчанию
        }

        books.append(new_book)

        flash("Книга успешно добавлена!", "success")
        return redirect(url_for("books_list"))

    return render_template("add_book.html", form=form)