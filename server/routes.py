import jndcontrollers
from app import app
from flask import request, jsonify, make_response
import requests
import maincontroller

#token_required = jndcontrollers.token_required
jnd = maincontroller.MainController()


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/')
def index():
    return "apples"
    # try:
    #     return requests.get('https://github.com/DavidDexterCharles?tab=repositories').content#, headers=headers).content
    # except:
    #     return "Welcome To JND(Rapid API Development with JSONERD Automation)"







'''
@app.route('/userauth', methods=['GET'])
@token_required
def getall_users_tokenrequired(current_user):
    # if jnd.isadmin(current_user):
    return jnd.getallusers()
    # else:
        # return jsonify({'message' : 'Cannot perform that function!'})

@app.route('/register', methods=['POST'])
def register_user():
    return jnd.doregister(request)
@app.route('/login', methods=['GET', 'POST'])
def login():
    return jnd.dologin(request)



#*****************************User***************************************

@app.route('/user', methods=['GET'])
def getall_users():
    return jnd.getallusers()
@app.route('/user/<id>', methods=['GET'])
def get_one_user(id):
    return jnd.getbyiduser(id)
@app.route('/user', methods=['POST'])
def create_user():
    return jnd.createuser(request)
@app.route('/user/<id>', methods=['PATCH'])
def update_user():
    return jnd.updateuser(request)
@app.route('/user', methods=['DELETE'])
def delete_user(id):
    return jnd.deleteuser(request)


'''

