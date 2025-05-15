# from time import sleep
#
# from flask import Blueprint, jsonify
#
# from src.config.status_enum import Status
# from src.driver.relay_driver import RelayDriver
# from src.driver.servo_driver import ServoDriver
#
# openapi = Blueprint('openapi', __name__)
#
#
# @openapi.route("/relay/<int:gpio>/<string:onoff>", methods=['GET'])
# def relay(onoff="off", gpio=25):
#     """
#     继电器开关控制 API
#     ---
#     tags:
#       - 继电器开关控制 API
#     parameters:
#       - name: gpio
#         in: path
#         type:  integer
#         required: true
#         description: 板子上 gpio 编号 如：G12,G13,G17,G18...
#       - name: onoff
#         in: path
#         type: string
#         required: true
#         description: 开 on , 关 off
#     responses:
#       500:
#         description: 指令错误
#       200:
#         description: 指令执行成功
#         schema:
#           id: R
#           properties:
#             code:
#               type: string
#               description: 状态码
#               default: "0000"
#     """
#     relay = RelayDriver(gpio)
#     if onoff.__eq__(Status.On.value.lower()):
#         relay.on()
#         info = "on"
#     elif onoff.__eq__(Status.Off.value.lower()):
#         relay.off()
#         info = "off"
#
#     return jsonify({"code": "0000", "info": "123"})
#
#
# @openapi.route("/servo/<int:gpio>/<int:angle>", methods=['GET'])
# def servo(angle=0, gpio=12):
#     """
#     舵机旋转角度控制 API
#     ---
#     tags:
#       - 舵机旋转角度控制 API
#     parameters:
#       - name: gpio
#         in: path
#         type:  integer
#         required: true
#         description: 板子上 gpio 编号 如：G12,G13,G17,G18...
#       - name: angle
#         in: path
#         type:  integer
#         required: true
#         description: 度数为整数 0,45,90,180,-45,-90,-180
#     responses:
#       500:
#         description: 度数错误
#       200:
#         description: 度数旋转完成
#         schema:
#           id: R
#           properties:
#             code:
#               type: string
#               description: 状态码
#               default: "0000"
#     """
#
#     servo = ServoDriver(gpio)
#     servo.start()
#     servo.angle(angle)
#     sleep(0.1)
#     servo.pause()
#     sleep(0.5)
#     servo.stop()
#     return jsonify({"code": "0000", "info": "123"})