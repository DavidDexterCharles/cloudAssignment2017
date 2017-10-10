from flask import Flask

app = Flask(__name__)

from routes import *

if __name__ == '__main__':
    # app.run()
    app.run(debug=True, port=8082,host="0.0.0.0")
