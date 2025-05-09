from flask import Blueprint

from src.driver.switch_driver import SwitchDriver

openapi = Blueprint('openapi', __name__)


@openapi.route("/switch/on")
def on():
    SwitchDriver(25).on()
    return ("pin 25 on")


@openapi.route("/switch/off")
def off():
    SwitchDriver(25).off()
    return "pin 25 off"
