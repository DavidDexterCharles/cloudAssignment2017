import os
from flask import Flask

app = Flask(__name__)

from routes import *

if __name__ == '__main__':
    # app.run()
    #app.run(debug=True, port=8082,host="0.0.0.0")
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8082)))# to run on cloud 9ide