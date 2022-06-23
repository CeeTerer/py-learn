from flask import Flask, render_template, request, Markup
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
choices = [0, 1, 2, 3, 4, 5]


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    url = StringField('Location URL', validators=[DataRequired(), URL()])
    open_time = StringField('Open time', validators=[DataRequired()])
    close_time = StringField('Closing time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=choices, validators=[DataRequired()], validate_choice=True)
    wifi_rating = SelectField('Wi-Fi rating', choices=choices, validators=[DataRequired()])
    power_rating = SelectField('power_outlet rating', choices=choices, validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    if request.method == 'POST':
        fields = ['Name', 'Location', 'Open Time', 'Close Time', 'Coffee Rating', 'Wifi Rating', 'Power Rating']
        cafe = form.cafe.data
        url = form.url.data
        open_time = form.open_time.data
        close_time = form.close_time.data
        coffee_rating = form.coffee_rating.data
        wifi_rating = form.coffee_rating.data
        power_rating = form.power_rating.data
        data_list = [cafe, url, open_time, close_time, coffee_rating, wifi_rating, power_rating]
        if form.validate_on_submit():
            with open('cafe-data.csv', 'a') as form_data:
                write = csv.writer(form_data)
                # write.writerow(fields)
                write.writerow(data_list)

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
