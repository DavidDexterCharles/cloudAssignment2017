import uuid
import datetime
from functools import wraps
# import jwt
from flask import Flask, request, jsonify, make_response
from azure.cosmosdb.table import TableService, Entity
import requests
import simplejson as json #https://simplejson.readthedocs.io/en/latest/
# from werkzeug.security import generate_password_hash, check_password_hash
# from models import app, User
headers = {'Content-Type': 'application/vnd.api+json'}
# apidomain = 'http://127.0.0.1:8085/api/'

table_service = TableService(account_name='comp69052017a216', account_key='6pWXbN/82hhsCKEcHEXdl0j5mxFcK6+lple/wYU29Jcb+kB55N/gAUuAd2PfL3mx67WxzJ8QxqhXbV5QdBG7iw==')

table_service.create_table('evenstore') 
table_service.create_table('materializedview') 


class UserJndController(object):
    pass

class WriteController(object):
    
    def createTransaction(self,request):
        data = json.dumps(request.get_json())
        d = json.loads(data)
        d['transtime']=str(datetime.datetime.utcnow())
        d['PartitionKey']=d['user']
        d['RowKey']=d['transtime']
        transaction = d
        table_service.insert_entity('evenstore', transaction)
        # return "fish"
        return json.dumps(d)

class ReadController(object):
   
    def getTransaction(self,request):
        data = json.dumps(request.get_json())
        d = json.loads(data)
        transactions = table_service.query_entities('evenstore', filter=" bank eq '"+d['bank']+"' and PartitionKey eq '"+d['user']+"'") # returns a set of trasactions fro a particular user and bank
        self.doreplay(transactions)
        return "app"
    

    def populateClientView(self):
        theview = []
        tasks = table_service.query_entities('materializedview')
        for task in tasks:
            theview.append({'user':task.customer, 'bank' : task.bank, 'balance' : task.balance})
        return json.dumps(theview)

    def doreplay(self,transactions): # replay and update user information for respective bank only in the materialized view
        i=0
        for t in transactions:
            if i==0:
                amt = 0
                user = t.user
                bank = t.bank
                i=1
            if t.trans=="Withdraw": 
                amt-=int(t.amount)
            if t.trans=="Deposit": 
                amt+=int(t.amount)
            # print t.user,t.bank,t.transtime,t.trans, t.amount ,amt
        m= json.loads(json.dumps({'customer' : user,'bank':bank,'balance':str(amt)}))
        m['PartitionKey']=str(user)
        m['RowKey']=str(bank)
        table_service.insert_or_replace_entity('materializedview', m)
        
          
