from flask_restful import Resource

from src.driver.ws2412d_driver import get_motor_instance


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
            description: 方向：前进 forward , 后退 reverse , 左转 turn_left , 右转 turn_right , 开始 start , 暂停 pause, 停止 stop
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
        ws2412d_motor = get_motor_instance()
        if direction.__eq__('forward'):
            ws2412d_motor.forward()
            ws2412d_motor.speed(speed, speed)
        elif direction.__eq__('reverse'):
            ws2412d_motor.reverse()
            ws2412d_motor.speed(speed, speed)
        elif direction.__eq__('turn_left'):
            ws2412d_motor.turn_left()
            ws2412d_motor.speed(speed, speed)
        elif direction.__eq__('turn_right'):
            ws2412d_motor.turn_right()
            ws2412d_motor.speed(speed, speed)
        elif direction.__eq__('start'):
            ws2412d_motor.start()
        elif direction.__eq__('pause'):
            ws2412d_motor.pause()
        elif direction.__eq__('stop'):
            ws2412d_motor.stop()

        return {"code": "0000"}
