from db_connection import get_data_from_db,signup_connection,get_recommendation
import flask
from flask_cors import CORS
import json
from flask import request

app = flask.Flask(__name__)
CORS(app)


@app.route('/login', methods =['GET', 'POST'])
def login():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        results = get_data_from_db(email, password)
        print(results)
        return results

@app.route('/signup', methods =['GET', 'POST'])
def signup():
    fullName = request.form["fullName"]
    email = request.form["email"]
    password = request.form["password"]
    confirmPassword = request.form["confirmPassword"]
    put_data = signup_connection(fullName,email,password,confirmPassword)
    print(put_data)
    return put_data

@app.route('/recommendation', methods =['GET', 'POST'])
def recommendation():
    streamName = request.form["streamName"]
    recommendation_list = get_recommendation(streamName)
    rec = json.dumps(recommendation_list, default=str)
    return rec



if __name__ == '__main__':
    app.run(host='127.0.0.1',port=54321)
