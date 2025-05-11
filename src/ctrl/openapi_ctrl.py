from flask import Blueprint, jsonify

from src.config.status_enum import Status
from src.driver.relay_driver import RelayDriver

openapi = Blueprint('openapi', __name__)


@openapi.route("/relay/<string:onoff>", methods=['GET'])
def on(onoff):
    """
    继电器开关控制 API
    ---
    tags:
      - 继电器开关控制 API
    parameters:
      - name: onoff
        in: path
        type: string
        required: true
        description: 开 on , 关 off
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
        schema:
          id: awesome
          properties:
            language:
              type: string
              description: The language name
              default: Lua
            features:
              type: array
              description: The awesomeness list
              items:
                type: string
              default: ["perfect", "simple", "lovely"]
    """

    if onoff == str(Status.On).lower():
        RelayDriver(25).on()
        info = "on"
    elif onoff == str(Status.Off).lower():
        RelayDriver(25).off()
        info = "off"

    return jsonify({"code": "0000", "info": "123"})
