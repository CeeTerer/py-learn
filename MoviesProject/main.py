from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
import requests
from flask_sqlalchemy import *
from sqlalchemy import *
import sqlite3
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    title = Column(String(80), unique=True, nullable=False)
    year = Column(Integer, unique=True, nullable=False)
    description = Column(String(255), nullable=False)
    rating = Column(Float, nullable=False)
    ranking = Column(Float, nullable=False)
    review = Column(String, nullable=False)
    img_url = Column(String(120), nullable=False)


class MovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    rating = StringField('rating', validators=[DataRequired()])
    ranking = StringField('ranking', validators=[DataRequired()])
    review = StringField('review', validators=[DataRequired()])
    img_url = StringField('img_url', validators=[DataRequired(), URL()])
    submit = SubmitField('Submit')


class RateMovie(FlaskForm):
    rating = StringField('New Rating', validators=[DataRequired()])
    review = StringField('Review')
    submit = SubmitField('Submit')


db.create_all()

all_movies = db.session.query(Movie).all()


@app.route("/")
def home():
    return render_template("index.html", all_movies=all_movies)


@app.route('/add', methods=['POST', 'GET'])
def add():
    add_movie = MovieForm()
    title = add_movie.title.data
    year = add_movie.year.data
    description = add_movie.description.data
    rating = add_movie.rating.data
    ranking = add_movie.ranking.data
    review = add_movie.review.data
    img_url = add_movie.img_url.data
    if add_movie.validate_on_submit():
        new_movie = Movie(title=title, year=year, description=description, rating=rating, ranking=ranking,
                          review=review, img_url=img_url)
        db.session.add(new_movie)
        db.session.commit()
        return render_template('index.html', all_movies=all_movies)
    return render_template('add.html', add_movie=add_movie)


@app.route('/edit/<int:index>', methods=['POST', 'GET'])
def edit(index):
    edit_form = RateMovie()
    requested_movie = None
    for movie in all_movies:
        if index == movie.id:
            requested_movie = movie
            new_rating = edit_form.rating.data
            new_review = edit_form.review.data
            if edit_form.validate_on_submit():
                requested_movie = Movie.query.get(requested_movie.id)
                requested_movie.rating = new_rating
                requested_movie.review = new_review
                db.session.commit()
                requested_movie = movie
                return render_template('index.html', all_movies=all_movies)
    return render_template('edit.html', edit_form=edit_form, requested_movie=requested_movie)


@app.route('/<int:index>')
def delete(index):
    requested_movie = None
    for movie in all_movies:
        if index == movie.id:
            requested_movie = movie
            requested_movie = Movie.query.get(requested_movie.id)
            db.session.delete(requested_movie)
            db.session.commit()
    return render_template('index.html', all_movies=all_movies)


if __name__ == '__main__':
    app.run(debug=True)
