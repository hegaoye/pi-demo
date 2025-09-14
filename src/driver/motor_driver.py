# coding=utf-8
from time import sleep

import RPi.GPIO as GPIO


class MotorDriver(object):
    """
    直流电机驱动
    """

    def __init__(self, pin1, pin2):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)  # 设置引脚编号系统，BOARD指的是物理引脚命名方式
        GPIO.setup(pin1, GPIO.OUT)  # 设置引脚
        GPIO.setup(pin2, GPIO.OUT)  # 设置引脚
        self.pwm1 = GPIO.PWM(pin1, 50)  # 创建电机pwm实例，并设置频率为50Hz
        self.pwm2 = GPIO.PWM(pin2, 50)  # 创建电机pwm实例，并设置频率为50Hz

    def start(self):
        """
        开始
        """
        self.pwm1.start(0)
        self.pwm2.start(0)

    def stop(self):
        """
        停止
        """
        self.pwm1.stop()
        self.pwm2.stop()

    def forward(self, pwm):
        """
        正转，pwm 控制速度
        """
        self.pwm1.ChangeDutyCycle(pwm)
        self.pwm2.ChangeDutyCycle(0)

    def reverse(self, pwm):
        """
        反转，pwm 控制速度
        """
        self.pwm1.ChangeDutyCycle(0)
        self.pwm2.ChangeDutyCycle(pwm)


if __name__ == '__main__':
    motor = MotorDriver(14, 15)
    motor.start()
    for pwm in range(35, 100):
        motor.forward(pwm)
        sleep(.2)

    for pwm in range(35, 100):
        motor.reverse(pwm)
        sleep(.2)

    motor.stop()
