import flask_restless
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_pyfile('config.cfg')


db = SQLAlchemy(app)

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)
    public_id = db.Column(db.String(50), unique=True)
    orders = db.relationship('Order', backref= 'user', lazy='dynamic')


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
restless_manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

if __name__ == '__main__':
    manager.run()
