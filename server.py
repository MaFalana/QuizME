from flask import Flask, jsonify, redirect, request
from flask_cors import CORS
from flask_cors import cross_origin
import requests

from db import DatabaseManager


db = DatabaseManager("QuizME")
users_collection = db.client['Users']

app = Flask(__name__) # Initialize the Flask application
CORS(app) # and enable CORS

@app.route('/', methods=['GET']) # Route to index page
@cross_origin()
def start():
    return jsonify({'message': 'Server is running.'})

@app.route('/register', methods=['POST']) # Route to register new users
@cross_origin()
def register():
    firstName = request.form['firstName'] # Extract form data
    lastName = request.form['lastName']
    displayName = request.form['displayName']
    email = request.form['email']
    password = request.form['password']

    #if db.query("users", {"email": email}).count() > 0: # Check if user already exists
    newUser = {
        "firstName": firstName,
        "lastName": lastName,
        "displayName": displayName,
        "email": email,
        "password": password,
        "Buddies": [],
        "Library": [],
    }

    db.insert("Users", newUser) # Insert new user into database in the Users collection
    

    return jsonify({'message': 'User successfully registered.'})

@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    data = request.form
    email = data['email']
    password = data['password']

    if users_collection.count_documents({"email": email, "password": password}) > 0:
        return jsonify({'message': 'User successfully logged in.'})
    else:
        return jsonify({'message': 'Invalid email or password.'})

if __name__ == '__main__':
    app.run() # Start the server when the script is run directly
    #app.run(host='0.0.0.0', port=5000)