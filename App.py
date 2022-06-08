from flask import Flask,jsonify,request
from data import data
app = Flask(__name__)
@app.route('/')

def index():
    return 'my name is Anish'

@app.route("/allplanet")
def planet():
    return jsonify({
        "data":data,
        "message":"success"
    })

@app.route("/specificplanet")
def specific_planet():
    name = request.args.get("name")
    planet_data = next(item for item in data if item["name"]==name)
    return jsonify({
        "data":planet_data
    })
if(__name__== '__main__'):

    app.run()