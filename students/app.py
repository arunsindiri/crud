from flask import Flask, jsonify, request
from database import create_table, adding_student, get_students, student_by_id

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

@app.route("/get_student/<int:id>", methods=["GET"])
def get_student_by_id(id):
    student = student_by_id(id)

    return jsonify(student)

@app.route("/show_students", methods=["GET"])
def show_students():
    students = get_students()
    
    return jsonify(students)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
