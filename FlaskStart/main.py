from flask import Flask

app = Flask(__name__)


def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"

    return wrapped


def italic(fn):
    def itali_wrapped():
        return "<i>" + fn() + "</i>"

    return itali_wrapped

@app.route("/")
@italic
def hello_world():
    return '<h1 Hello, World!</h1>' \
           '<p> This is a paragrah </p>'


@app.route("/bye")
@make_bold
def bye():
    return "Bye"


@app.route("/<name>")
def greet(name):
    return f"Hello {name}"


if __name__ == "__main__":
    app.run(debug=True)
