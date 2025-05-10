from flask import Blueprint, jsonify

from src.driver.relay_driver import RelayDriver

openapi = Blueprint('openapi', __name__)


@openapi.route("/relay/on", methods=['GET'])
def on():
    RelayDriver(25).on()
    return jsonify({"code": "0000", "info": "on"})


@openapi.route("/relay/off", methods=['GET'])
def off():
    RelayDriver(25).off()
    return jsonify({"code": "0000", "info": "off"})
