from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY']='7550673a81fc6dbce40035f5'

from app import routes