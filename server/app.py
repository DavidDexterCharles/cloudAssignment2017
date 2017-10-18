import os
from flask import Flask,render_template
from flask_socketio import SocketIO, emit
app = Flask(__name__,template_folder='../client')
app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'

socketio = SocketIO( app )
from routes import *

if __name__ == '__main__':
    # app.run()
    # app.run(debug=True, port=8082)
    socketio.run( app, debug = True,port=8082)
    # app.run(debug=True, port=8082,host="0.0.0.0")
    # app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8082)))# to run on cloud 9ide