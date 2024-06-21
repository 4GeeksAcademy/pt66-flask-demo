from flask import Flask
from src.contacts import api as contacts_api

app = Flask(__name__)
app.register_blueprint(contacts_api)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    return """<h1>Hello world!</h1>"""


@app.route("/error")
def throw_error():
    raise Exception("Oh no, something broke!")
