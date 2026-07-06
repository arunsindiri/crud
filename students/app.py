from flask import Flask, jsonify, request
from database import create_table, adding_student

app = Flask(__name__)

create_table()

@app.route("/")
def home():
    return jsonify ({"message":"Student database connected sucessfully"})

@app.route("/add_student", methods=["POST"])
def add_student():
    data = request.get_json()

    name = data["name"]
    age = data["age"]
    course = data["course"] 

    adding_student(name, age, course)

    return jsonify({"message":"Student added sucessfully"})  

if __name__ == "__main__":
    app.run(debug=True, port=8000)
