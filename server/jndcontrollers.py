import uuid
import datetime
from functools import wraps
# import jwt
from flask import Flask, request, jsonify, make_response
import requests
import simplejson as json #https://simplejson.readthedocs.io/en/latest/
# from werkzeug.security import generate_password_hash, check_password_hash
# from models import app, User
headers = {'Content-Type': 'application/vnd.api+json'}
# apidomain = 'http://127.0.0.1:8085/api/'


class UserJndController(object):
    pass

class WriteController(object):
    
    def createTransaction(self,request):
        data = json.dumps(request.get_json())
        d = json.loads(data)
        d['transtime']=str(datetime.datetime.utcnow())
        return json.dumps(d)