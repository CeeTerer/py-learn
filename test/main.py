from flask import Flask
from random import randint

app = Flask(__name__)

random_number = randint(0, 9)


@app.route('/')
def make_a_guess():
    return "Guess a number between 0 and 9"


@app.route('/<int:guess>')
def check_guess(guess):
    if guess > random_number:
        return "<h1>Too high! Try again</h1>"

    if guess < random_number:
        return "<h1 style=color: purple>Too Low! Try again </h>"

    else:
        return "<h1>Correct</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
