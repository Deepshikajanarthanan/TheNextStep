from db_connection import get_data_from_db,signup_connection,get_recommendation,get_stream_info,dump_data_to_db
import flask
from flask_cors import CORS
import json
from flask import request

app = flask.Flask(__name__)
CORS(app)


@app.route('/login', methods =['GET', 'POST'])
def login():
    data = request.get_json(force=True)
    email = data['email']
    password = data['password']
    results = get_data_from_db(email, password)
    return results

@app.route('/signup', methods =['GET', 'POST'])
def signup():
    data = request.get_json(force=True)
    fullName = data['fullName']
    email = data['email']
    password = data['password']
    confirmPassword = data['confirmPassword']
    put_data = signup_connection(fullName,email,password,confirmPassword)
    return put_data

@app.route('/recommendation', methods =['GET', 'POST'])
def recommendation():
    data = request.get_json(force=True)
    streamName = data["streamName"]
    recommendation_list = get_recommendation(streamName)
    rec = json.dumps(recommendation_list, default=str)
    return rec

@app.route('/chartApi', methods =['GET', 'POST'])
def chartApi():
    data = request.get_json(force=True)
    streamName = data["streamName"]
    perc_of_stream = get_stream_info(streamName)
    print(perc_of_stream)
    count_of_stream = json.dumps(perc_of_stream, default=str)
    return count_of_stream

@app.route('/formData', methods =['GET', 'POST'])
def formData():
    data = request.get_json(force=True)
    formData = data["formData"]
    dump_data = dump_data_to_db(formData)
    return dump_data

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=54321)