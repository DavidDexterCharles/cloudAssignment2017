import uuid
import datetime
from functools import wraps
from flask import Flask, request, jsonify, make_response
from azure.cosmosdb.table import TableService, Entity
import requests
import simplejson as json #https://simplejson.readthedocs.io/en/latest/
headers = {'Content-Type': 'application/vnd.api+json'}


table_service = TableService(account_name='comp69052017a216', account_key='')

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
        return json.dumps(d)

    def getEventStore(self):
        theevents = []
        tasks = table_service.query_entities('evenstore')
        for task in tasks:
            theevents.append({'PartitionKey':task.PartitionKey, 'RowKey' : task.RowKey,'User' : task.user,'Bank' : task.bank,'Transaction' : task.trans,'Amount' : task.amount, 'TransTime' : task.transtime})
        return json.dumps(theevents)

class ReadController(object):
   
    def updateView(self,request):
        data = json.dumps(request.get_json())
        d = json.loads(data)
        transactions = table_service.query_entities('evenstore', filter=" bank eq '"+d['bank']+"' and PartitionKey eq '"+d['user']+"'") # returns a set of trasactions fro a particular user and bank
        self.doreplay(transactions)
        return "app"
   
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

     

    def populateClientView(self):
        theview = []
        tasks = table_service.query_entities('materializedview')
        for task in tasks:
            theview.append({'user':task.customer, 'bank' : task.bank, 'balance' : task.balance})
        return json.dumps(theview)
        
          
