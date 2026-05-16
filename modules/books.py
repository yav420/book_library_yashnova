from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db, Book
from forms import BookForm

books_bp = Blueprint('books', __name__, template_folder='../templates/books')


@books_bp.route("/books")
def books_list():
    books = Book.query.all()
    return render_template("books_list.html", books=books)


@books_bp.route("/books/<int:book_id>")
def book_detail(book_id):
    book = db.get_or_404(Book, book_id)
    return render_template("book_detail.html", book=book)


@books_bp.route("/search")
def search():
    q = request.args.get("q", "").strip()
    if not q:
        return render_template("search.html", q=None, results=None)

    results = Book.query.filter(
        db.or_(Book.title.ilike(f"%{q}%"), Book.author.ilike(f"%{q}%"))
    ).all()
    return render_template("search.html", q=q, results=results)


@books_bp.route("/add-book", methods=["GET", "POST"])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        new_book = Book(
            title=form.title.data,
            author=form.author.data,
            genre=form.genre.data,
            year=form.year.data,
            description=form.description.data,
            cover=form.cover_filename.data or "placeholder.png"
        )
        db.session.add(new_book)
        db.session.commit()
        flash("Книга успешно добавлена!", "success")
        return redirect(url_for("books.books_list"))
    return render_template("add_book.html", form=form)