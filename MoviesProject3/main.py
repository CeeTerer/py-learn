from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_sqlalchemy import *
from sqlalchemy import *
import requests

API_KEY = '932037e00c2b5a6af5195f8ad77b66ba'
# API_LINK = 'https://api.themoviedb.org/3/search/movie'
# PARAMS = {
#     'api_key' : API_KEY,
#     'query' : 'Spiderman no way home'
# }

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
    year = Column(String(80), nullable=False)
    description = Column(String(120), nullable=False)
    rating = Column(Float)
    ranking = Column(Float)
    review = Column(String)
    img_url = (Column(String(80)))


class MovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RateMovie(FlaskForm):
    rating = StringField('rating', validators=[DataRequired()])
    submit = SubmitField('Submit')


db.create_all()

all_movies = db.session.query(Movie).all()


@app.route("/")
def home():
    return render_template("index.html", all_movies=all_movies)


@app.route('/select', methods=['POST', 'GET'])
def select():
    add_movie = MovieForm()
    requested_title = add_movie.title.data
    if add_movie.validate_on_submit():
        response = requests.get(
            f'https://api.themoviedb.org/3/search/keyword?api_key=932037e00c2b5a6af5195f8ad77b66ba&query={requested_title}&page=1').json()
        movies = response['results']
        print(movies)
        return render_template('select.html', movies=movies, add_movie=add_movie)
    return render_template('add.html', add_movie=add_movie)


@app.route('/add', methods=['POST', 'GET'])
def add():
    # request.args.get('')
    response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=932037e00c2b5a6af5195f8ad77b66ba'
                            f'&language=en-US&page=1&include_adult=false&query=daytona 500').json()
    data = response['results'][0]
    title = data['title']
    description = data['overview']
    year = data['release_date'].split('-')[0]
    img_path = data['poster_path']
    img_url = f'http://image.tmdb.org/t/p/w500/{img_path}'
    new_movie = Movie(title=title, year=year, description=description, img_url=img_url)
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', index=new_movie.id))


@app.route('/edit/<int:index>', methods=['POST', 'GET'])
def edit(index):
    edit_form = RateMovie()
    requested_movie = Movie.query.get(index)
    if edit_form.validate_on_submit():
        new_rating = edit_form.rating.data
        requested_movie.rating = new_rating
        db.session.commit()
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


#
# @app.route('/select', methods=['POST', 'GET'])
# def select():
#     add_movie = MovieForm()
#     requested_title = add_movie.title.data
#     print(requested_title)
#     response = requests.get(f'https://api.themoviedb.org/3/search/keyword?api_key=932037e00c2b5a6af5195f8ad77b66ba&query={requested_title}&page=1').json()
#     print(response)
#     return render_template('select.html')

if __name__ == '__main__':
    app.run(debug=True)
