from flask_restful import Resource

from src.config.status_enum import Status
from src.driver.relay_driver import RelayDriver


class RelayResource(Resource):
    """
    继电器开关控制
    """

    def get(self, onoff="off", gpio=25):
        """
        继电器开关控制 API
        ---
        tags:
          - 继电器开关控制 API
        parameters:
          - name: gpio
            in: path
            type:  integer
            required: true
            description: 板子上 gpio 编号 如：G12,G13,G17,G18...
          - name: onoff
            in: path
            type: string
            required: true
            description: 开 on , 关 off
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
        relay = RelayDriver(gpio)
        if onoff.__eq__(Status.On.value.lower()):
            relay.on()
            info = "on"
        elif onoff.__eq__(Status.Off.value.lower()):
            relay.off()
            info = "off"

        return {"code": "0000", "info": info}
