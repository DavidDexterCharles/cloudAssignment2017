import jndcontrollers
import simplejson as json
from app import app,  socketio, render_template
from flask import Flask,request, jsonify, make_response
import requests
import maincontroller
headers = {'Content-Type': 'application/json'}
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
    return render_template('app.html')
   
@app.route('/events')
def getEvents():
    return render_template('events.html')
    # return render_template('app.html')

@app.route('/transaction',methods=['GET', 'POST'])
def getonetrans():
    if request.method == 'GET':
         return jsonify({"name":"Lord Of The Rings","type":"Adventure"},{"name":"Dishonored","type":"Stealth"})
    if request.method == 'POST':
        # print request.data
        # return request.data
        result=jnd.createTransaction(request)
        val = jnd.updateView(request)
        return result

def messageRecived():
  print 'message was received!!!' 

@socketio.on( 'my event' )
def handle_my_custom_event( data ):
    # print 'recived my event: ' + json.dumps(data )
    data1 = json.dumps(data )
    data2= requests.post('http://localhost:8082/transaction', data1, headers=headers).content 
    #   print json.loads(data)
    data3 = jnd.populateClientView()
    # print data3
    socketio.emit( 'my response', data3, callback=messageRecived )


@socketio.on( 'get event')
def handle_my_eventstore_events( data ):
    data= jnd.getEventStore() 
    socketio.emit( 'getevent response', data, callback=messageRecived )
