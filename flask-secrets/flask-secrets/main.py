from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
import email_validator
from flask_bootstrap import Bootstrap


class PhotoForm(FlaskForm):
    email = StringField(label='Email', validators=[Email(check_deliverability=True, )])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(max=8)])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'kjvsbqjabdn'


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = PhotoForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            return render_template('success.html')
        else:
            return render_template('denied.html')
    else:
        return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
