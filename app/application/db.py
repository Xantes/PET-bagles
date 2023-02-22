from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from application.app import app


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Sessions(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    session_id = db.Column(db.String(40), unique=True)
    user = db.Column(db.Text)
    number = db.Column(db.String(3))
    tries = db.Column(db.Integer)
    finish = db.Column(db.Boolean)


class Languages(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    language = db.Column(db.String(40))
    greetings_msg = db.Column(db.String(128))
    win_msg = db.Column(db.String(128))
    fail_msg = db.Column(db.String(128))
    last_try_msg = db.Column(db.String(128))


with app.app_context():
    db.create_all()
