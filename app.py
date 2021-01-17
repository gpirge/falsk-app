from flask import Flask
from flask import request
app = Flask(__name__)

# http://127.0.0.1:5000/users/anything -> Base Url

@app.route('/')
def index():
    return "Hello Flask"

@app.route('/users/<user_id>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def parameter(user_id):
    if request.method == 'GET':
        return 'GET method'

    elif request.method == 'POST':
        data = request.form
        return 'POST method'

    elif request.method == 'PUT':
        return 'PUT method'

    elif request.method == 'DELETE':
        return 'DELETE method'
    else:
        return 'no such method'

    return user_id

app.run()
