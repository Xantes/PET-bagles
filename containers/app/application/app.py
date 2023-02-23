from flask import Flask
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config.from_object('config')

bootsrap = Bootstrap5(app)
