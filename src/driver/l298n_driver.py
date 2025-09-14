# coding=utf-8

import RPi.GPIO as GPIO


class L298NMotorDriver(object):
    """
    直流电机驱动器驱动
    """

    def __init__(self, in1, in2, in3, in4):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)  # 设置引脚编号系统，BOARD指的是物理引脚命名方式

        # ENA
        GPIO.setup(in1, GPIO.OUT)  # 设置引脚
        GPIO.setup(in2, GPIO.OUT)  # 设置引脚

        # ENB
        GPIO.setup(in3, GPIO.OUT)  # 设置引脚
        GPIO.setup(in4, GPIO.OUT)  # 设置引脚

        self.pwm1 = GPIO.PWM(in1, 50)  # 创建电机pwm实例，并设置频率为50Hz
        self.pwm2 = GPIO.PWM(in2, 50)  # 创建电机pwm实例，并设置频率为50Hz
        self.pwm3 = GPIO.PWM(in3, 50)  # 创建电机pwm实例，并设置频率为50Hz
        self.pwm4 = GPIO.PWM(in4, 50)  # 创建电机pwm实例，并设置频率为50Hz

    def start(self):
        """
        开始
        """
        self.pwm1.start(0)
        self.pwm2.start(0)
        self.pwm3.start(0)
        self.pwm4.start(0)

    def stop(self):
        """
        停止
        """
        self.pwm1.stop()
        self.pwm2.stop()
        self.pwm3.stop()
        self.pwm4.stop()

    def forward(self, pwm):
        """
        正转，pwm 控制速度
        """
        # ENA
        self.pwm1.ChangeDutyCycle(pwm)
        self.pwm2.ChangeDutyCycle(0)
        # ENB
        self.pwm3.ChangeDutyCycle(pwm)
        self.pwm4.ChangeDutyCycle(0)

    def reverse(self, pwm):
        """
        反转，pwm 控制速度
        """
        # ENA
        self.pwm1.ChangeDutyCycle(0)
        self.pwm2.ChangeDutyCycle(pwm)
        # ENB
        self.pwm3.ChangeDutyCycle(0)
        self.pwm4.ChangeDutyCycle(pwm)

    def turn_left(self, pwm):
        """
        左转
        """
        # ENA
        self.pwm1.ChangeDutyCycle(0)
        self.pwm2.ChangeDutyCycle(0)
        # ENB
        self.pwm3.ChangeDutyCycle(pwm)
        self.pwm4.ChangeDutyCycle(0)

    def turn_right(self, pwm):
        """
        右转
        """
        # ENA
        self.pwm1.ChangeDutyCycle(pwm)
        self.pwm2.ChangeDutyCycle(0)
        # ENB
        self.pwm3.ChangeDutyCycle(0)
        self.pwm4.ChangeDutyCycle(0)
