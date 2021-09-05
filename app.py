# import Flask dependency
from flask import Flask

#Creat new Flask app instance
app = Flask(__name__)

#Create Flask routes
@app.route('/')
def hello_world():
    return "Hello World"