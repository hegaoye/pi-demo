from flask import Blueprint

from src.driver.relay_driver import RelayDriver

openapi = Blueprint('openapi', __name__)


@openapi.route("/relay/on")
def on():
    RelayDriver(25).on()
    return ("pin 25 on")


@openapi.route("/relay/off")
def off():
    RelayDriver(25).off()
    return "pin 25 off"
