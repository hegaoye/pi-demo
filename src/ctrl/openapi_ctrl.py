from flask import Blueprint, jsonify

from src.config.status_enum import Status
from src.driver.relay_driver import RelayDriver

openapi = Blueprint('openapi', __name__)


@openapi.route("/relay/<onoff>", methods=['GET'])
def on(onoff):
    if onoff == str(Status.On).lower():
        RelayDriver(25).on()
        info = "on"
    elif onoff == str(Status.Off).lower():
        RelayDriver(25).off()
        info = "off"

    return jsonify({"code": "0000", "info": info})
