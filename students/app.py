from flask import Flask, jsonify
from database import create_table

app = Flask(__name__)

create_table()

@app.route("/")
def home():
    return jsonify ({"message":"Student database connected sucessfully"})

if __name__ == "__main__":
    app.run(debug=True, port=8000)
