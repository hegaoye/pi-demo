from flask import request
from flask_restful import Resource

from src.driver.button_driver import ButtonDriver


class ButtonResource(Resource):
    """
    机械开关控制
    """

    def get(self, gpio=26):
        """
        机械开关控制 API
        ---
        tags:
          - 机械开关控制 API
        parameters:
          - name: gpio
            in: path
            type:  integer
            required: true
            description: 板子上 gpio 编号 如：G12,G13,G17,G18...
          - name: callback
            in: parameter
            type: string
            required: true
            description: 回调通知地址
        responses:
          500:
            description: 指令错误
          200:
            description: 指令执行成功
            schema:
              id: R
              properties:
                code:
                  type: string
                  description: 状态码
                  default: "0000"
        """
        callback = request.args.get("callback")

        button_driver = ButtonDriver(gpio, callback)
        button_driver.read()
        return {"code": "0000", "info": callback}


def callback():
    pass
