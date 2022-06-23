from flask import Flask, render_template, redirect, url_for, request
import sqlite3
from flask_sqlalchemy import *
from sqlalchemy import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    author = Column(String(120), unique=True, nullable=False)
    rating = Column(Float, nullable=False)


db.create_all()

all_books = db.session.query(Book).all()


# db = sqlite3.connect("books-collection.db") cursor = db.cursor() # cursor.execute("CREATE TABLE library (id INTEGER
# PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) " #                "NOT NULL, rating FLOAT NOT
# NULL)") cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')") db.commit()

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html', all_books=all_books)


@app.route('/edit/<int:index>', methods=['POST', 'GET'])
def edit(index):
    # rating_to_update = Book.query.get(index)
    for book in all_books:
        queried_book = None
        print(book.rating)
        if request.method == "POST":
            # rating_to_update = db.session.query(Book).filter_by(book.id)
            # rating_to_update.rating = request.form.get('rating')
            # db.session.commit()
            book.rating = request.form.get('rating')
            print(request.form.get('rating'))
            return render_template("index.html", queried_book=queried_book)
        if book.id == index:
            queried_book = book
        return render_template("edit.html", queried_book=queried_book)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        id = Column(Integer, primary_key=True)
        name = request.form.get('name')
        author = request.form.get('author')
        rating = request.form.get('rating')
        new_book = Book(id=id, name=name, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)
