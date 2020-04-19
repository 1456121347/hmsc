    
from flask import *
from hmsc import app

@app.route("/")
def index():

    return 'hello'