# coding=utf-8
from time import sleep

import RPi.GPIO as GPIO

ENA = 15
IN1 = 4
IN2 = 14

ENB = 24
IN3 = 22
IN4 = 23

# 全局电机实例，用于持续控制
l298n_motor = None


def get_motor_instance():
    """
    实现单例模式
    """
    global l298n_motor
    if l298n_motor is None:
        l298n_motor = L298NMotorDriver()
        l298n_motor.start()
    return l298n_motor


class L298NMotorDriver(object):
    """
    直流电机驱动器驱动
    """

    def __init__(self, ena_pin=ENA, in1_pin=IN1, in2_pin=IN2, enb_pin=ENB, in3_pin=IN3, in4_pin=IN4):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        # ENA
        GPIO.setup(ena_pin, GPIO.OUT)  # 设置引脚
        GPIO.setup(in1_pin, GPIO.OUT)  # 设置引脚
        GPIO.setup(in2_pin, GPIO.OUT)  # 设置引脚

        # ENB
        GPIO.setup(enb_pin, GPIO.OUT)  # 设置引脚
        GPIO.setup(in3_pin, GPIO.OUT)  # 设置引脚
        GPIO.setup(in4_pin, GPIO.OUT)  # 设置引脚

        self.ena_pin = GPIO.PWM(ena_pin, 100)  # 创建电机pwm实例，并设置频率为100Hz
        self.enb_pin = GPIO.PWM(enb_pin, 100)  # 创建电机pwm实例，并设置频率为100Hz

        self.in1_pin = in1_pin
        self.in2_pin = in2_pin
        self.in3_pin = in3_pin
        self.in4_pin = in4_pin

    def start(self):
        """
        开始
        """
        # 默认设置0频率
        self.ena_pin.start(0)
        self.enb_pin.start(0)
        GPIO.output(self.in1_pin, GPIO.LOW)
        GPIO.output(self.in2_pin, GPIO.LOW)
        GPIO.output(self.in3_pin, GPIO.LOW)
        GPIO.output(self.in4_pin, GPIO.LOW)

    def pause(self):
        self.ena_pin.ChangeDutyCycle(0)
        self.enb_pin.ChangeDutyCycle(0)
        GPIO.output(self.in1_pin, GPIO.LOW)
        GPIO.output(self.in2_pin, GPIO.LOW)
        GPIO.output(self.in3_pin, GPIO.LOW)
        GPIO.output(self.in4_pin, GPIO.LOW)

    def stop(self):
        """
        停止
        """
        self.ena_pin.stop()
        self.enb_pin.stop()
        GPIO.output(self.in1_pin, False)
        GPIO.output(self.in2_pin, False)
        GPIO.output(self.in3_pin, False)
        GPIO.output(self.in4_pin, False)

    def forward(self, pwm):
        """
        正转，pwm 控制速度
        """
        # ENA
        self.ena_pin.ChangeDutyCycle(pwm)
        GPIO.output(self.in1_pin, GPIO.HIGH)
        GPIO.output(self.in2_pin, GPIO.LOW)
        # ENB
        self.enb_pin.ChangeDutyCycle(pwm)
        GPIO.output(self.in3_pin, GPIO.HIGH)
        GPIO.output(self.in4_pin, GPIO.LOW)

    def reverse(self, pwm):
        """
        反转，pwm 控制速度
        """
        # ENA
        self.ena_pin.ChangeDutyCycle(pwm)
        GPIO.output(self.in1_pin, GPIO.LOW)
        GPIO.output(self.in2_pin, GPIO.HIGH)
        # ENB
        self.enb_pin.ChangeDutyCycle(pwm)
        GPIO.output(self.in3_pin, GPIO.LOW)
        GPIO.output(self.in4_pin, GPIO.HIGH)

    def turn_left(self, pwm):
        """
        左转
        """
        # ENA
        self.ena_pin.ChangeDutyCycle(pwm)
        GPIO.output(self.in1_pin, GPIO.LOW)
        GPIO.output(self.in2_pin, GPIO.HIGH)
        # ENB
        self.enb_pin.ChangeDutyCycle(pwm)
        GPIO.output(self.in3_pin, GPIO.HIGH)
        GPIO.output(self.in4_pin, GPIO.LOW)

    def turn_right(self, pwm):
        """
        右转
        """
        # ENA
        self.ena_pin.ChangeDutyCycle(pwm)
        GPIO.output(self.in1_pin, GPIO.HIGH)
        GPIO.output(self.in2_pin, GPIO.LOW)
        # ENB
        self.enb_pin.ChangeDutyCycle(pwm)
        GPIO.output(self.in3_pin, GPIO.LOW)
        GPIO.output(self.in4_pin, GPIO.HIGH)


if __name__ == '__main__':
    l298n_motor = L298NMotorDriver()
    l298n_motor.start()
    l298n_motor.forward(100)
    sleep(10)
    l298n_motor.reverse(100)
    sleep(10)
    l298n_motor.turn_left(100)
    sleep(10)
    l298n_motor.turn_right(100)
    sleep(10)
    l298n_motor.stop()
