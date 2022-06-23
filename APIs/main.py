from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route('/random', methods=['GET'])
def get_random_cafe():
      cafes = db.session.query(Cafe).all()
      random_cafe = random.choice(cafes)
      return jsonify(cafe_name=random_cafe.name,can_take_calls=random_cafe.can_take_calls,coffee_price=random_cafe.coffee_price,has_sockets=random_cafe.coffee_price,has_toilets=random_cafe.has_toilet,
      has_wifi=random_cafe.has_wifi, id=random_cafe.id, img_url=random_cafe.img_url,location=random_cafe.location, map_url=random_cafe.map_url, seats=random_cafe.seats)

@app.route('/all', methods=['GET'])   
def get_all_cafes():
    cafes = db.session.query(Cafe).all() 
    all_cafes = []
    for cafe in cafes:
        cafe_data = {"cafe_name":cafe.name, "can_take_calls":cafe.can_take_calls, "coffee_price":cafe.coffee_price, "has_sockets":cafe.coffee_price, "has_toilets":cafe.has_toilet,
        "has_wifi":cafe.has_wifi, "id":cafe.id, "img_url": cafe.img_url, "location": cafe.location, "map_url":cafe.map_url, "seats":cafe.seats}
        all_cafes.append(cafe_data)    
    cafes = {"cafes": all_cafes}
    json_data = jsonify(cafes)
        
    return json_data

@app.route('/search', methods=['GET'])
def search():
    query_location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
  
    if cafe:
        return jsonify(cafe_name=cafe.name,can_take_calls=cafe.can_take_calls,coffee_price=cafe.coffee_price,has_sockets=cafe.coffee_price,has_toilets=cafe.has_toilet,
      has_wifi=cafe.has_wifi, id=cafe.id, img_url=cafe.img_url,location=cafe.location, map_url=cafe.map_url, seats=cafe.seats)
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})

## HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add():
    return jsonify(response= {"success": "Cafe added"})



## HTTP PUT/PATCH - Update Record
@app.route('/update_price/<int:cafe_id>', methods=['GET','PATCH'])
def patch(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe and new_price:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response= {"success": "Price_updated successfully"})
    else:
        return jsonify( error= {"Data Required": "Please be sure to add cafe id and the new price."})
## HTTP DELETE - Delete Record
@app.route('/report_closed/<int:cafe_id>',methods=['GET','DELETE'])
def delete(cafe_id):
    api_key = request.args.get('api_key') 
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe and api_key:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response= {"success": "deleted successfully"})
    else:
        jsonify(response= {"Fail": "delete unsuccessfully"})
if __name__ == '__main__':
    app.run(debug=True)
