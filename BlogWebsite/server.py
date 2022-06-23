from flask import Flask, render_template
import random
from time import time
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    year = datetime.datetime.today().year
    return render_template('index.html', year=year)


@app.route('/guess/<yourname>')
def guess(yourname):
    gender_response = requests.get(f"https://api.genderize.io?name={yourname}").json()
    gender = gender_response["gender"]
    age_response = requests.get(f"https://api.agify.io/?name={yourname}").json()
    age = age_response["age"]
    name = yourname.title()
    return render_template('guess.html', age=age, gender=gender, name=name)


@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_posts = requests.get(blog_url).json()
    return render_template('blog.html', posts=blog_posts)


if __name__ == "__main__":
    app.run(debug=True)
