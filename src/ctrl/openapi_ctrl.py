from flask import Blueprint

openapi = Blueprint('openapi', __name__)

@openapi.route("/")
def hello():
    return "Hello World!"
