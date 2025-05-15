from time import sleep

from flask_restful import Resource

from src.driver.servo_driver import ServoDriver


class ServoResource(Resource):
    """
    舵机旋转角度控制
    """

    def get(self, angle=0, gpio=12):
        """
        舵机旋转角度控制 API
        ---
        tags:
          - 舵机旋转角度控制 API
        parameters:
          - name: gpio
            in: path
            type:  integer
            required: true
            description: 板子上 gpio 编号 如：G12,G13,G17,G18...
          - name: angle
            in: path
            type:  integer
            required: true
            description: 度数为整数 0,45,90,180,-45,-90,-180
        responses:
          500:
            description: 度数错误
          200:
            description: 度数旋转完成
            schema:
              id: R
              properties:
                code:
                  type: string
                  description: 状态码
                  default: "0000"
        """

        servo = ServoDriver(gpio)
        servo.start()
        servo.angle(angle)
        sleep(0.1)
        servo.pause()
        sleep(0.5)
        servo.stop()
        return {"code": "0000"}
