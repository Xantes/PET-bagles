from application import views
from application.app import app
from application import db
from application import game

from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()
csrf.init_app(app)
