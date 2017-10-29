import jndcontrollers
import simplejson as json
from app import app,  socketio, render_template
from flask import Flask,request, jsonify, make_response
import requests
import maincontroller
headers = {'Content-Type': 'application/json'}
jnd = maincontroller.MainController()


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/')
def index():
    return render_template('app.html')
   
@app.route('/events')
def getEvents():
    return render_template('events.html')
    

@app.route('/transaction',methods=['POST'])
def add_transaction_to_eventstore():
    if request.method == 'POST':
        result=jnd.createTransaction(request)
        jnd.updateView(request)# update the materialized view stored in an azure table called materializedview
        return result

def messageRecived():
  print 'message was received!!!' 

@socketio.on( 'my event' )
def handle_my_custom_event( data ):
    data1 = json.dumps(data )
    data2= requests.post('http://localhost:8082/transaction', data1, headers=headers).content 
    data3 = jnd.populateClientView()# gets the data from the azure table that stored the view to display on UI
    socketio.emit( 'my response', data3, callback=messageRecived )# broadcast the event, and updates all users UI


@socketio.on( 'get event')
def handle_my_eventstore_events( data ):
    data= jnd.getEventStore() 
    socketio.emit( 'getevent response', data, callback=messageRecived )
