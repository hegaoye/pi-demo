from time import sleep

from flask_restful import Resource

from src.driver.l298n_driver import L298NMotorDriver

# 全局电机实例，用于持续控制
l298n_motor = None


def get_motor_instance():
    global l298n_motor
    if l298n_motor is None:
        l298n_motor = L298NMotorDriver()
        l298n_motor.start()
    return l298n_motor


class ChassisResource(Resource):
    """
    底盘控制
    """

    def get(self, direction='forward', speed=0):
        """
        底盘控制 API
        ---
        tags:
          - 底盘控制 API
        parameters:
          - name: direction
            in: path
            type:  string
            required: true
            description: 方向：前进 forward,后退 reverse，左转 turn_left，右转 turn_right;默认 forward
          - name: speed
            in: path
            type:  integer
            required: true
            description: 速度，0~100，默认 0
        responses:
          500:
            description: 参数错误
          200:
            description: 正确执行
            schema:
              id: R
              properties:
                code:
                  type: string
                  description: 状态码
                  default: "0000"
        """
        l298n_motor = get_motor_instance()
        if direction.__eq__('forward'):
            l298n_motor.forward(speed)
        elif direction.__eq__('reverse'):
            l298n_motor.reverse(speed)
        elif direction.__eq__('turn_left'):
            l298n_motor.turn_left(speed)
        elif direction.__eq__('turn_right'):
            l298n_motor.turn_right(speed)
        else:
            l298n_motor.pause()

        return {"code": "0000"}
