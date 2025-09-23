# coding=utf-8

import RPi.GPIO as GPIO


class L298NMotorDriver(object):
    """
    直流电机驱动器驱动
    """

    def __init__(self, ena_pin, in1_pin, in2_pin, enb_pin, in3_pin, in4_pin):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)  # 设置引脚编号系统，BOARD指的是物理引脚命名方式

        # ENA
        GPIO.setup(ena_pin, GPIO.OUT)  # 设置引脚
        GPIO.setup(in1_pin, GPIO.OUT)  # 设置引脚
        GPIO.setup(in2_pin, GPIO.OUT)  # 设置引脚

        # ENB
        GPIO.setup(enb_pin, GPIO.OUT)  # 设置引脚
        GPIO.setup(in3_pin, GPIO.OUT)  # 设置引脚
        GPIO.setup(in4_pin, GPIO.OUT)  # 设置引脚

        self.ena_pin = GPIO.PWM(ena_pin, 50)  # 创建电机pwm实例，并设置频率为50Hz
        self.enb_pin = GPIO.PWM(enb_pin, 50)  # 创建电机pwm实例，并设置频率为50Hz
        # 默认设置0频率
        self.ena_pin.ChangeDutyCycle(0)
        self.enb_pin.ChangeDutyCycle(0)

        self.in1_pin = GPIO.output(in1_pin, GPIO.LOW)  # 创建电机pwm实例，并设置频率为50Hz
        self.in2_pin = GPIO.output(in2_pin, GPIO.LOW)  # 创建电机pwm实例，并设置频率为50Hz

        self.in3_pin = GPIO.output(in3_pin, GPIO.LOW)  # 创建电机pwm实例，并设置频率为50Hz
        self.in4_pin = GPIO.output(in4_pin, GPIO.LOW)  # 创建电机pwm实例，并设置频率为50Hz

    def start(self):
        """
        开始
        """
        # 默认设置0频率
        self.ena_pin.ChangeDutyCycle(0)
        self.enb_pin.ChangeDutyCycle(0)
        self.in1_pin.start(0)
        self.in2_pin.start(0)
        self.in3_pin.start(0)
        self.in4_pin.start(0)

    def stop(self):
        """
        停止
        """
        self.in1_pin.stop()
        self.in2_pin.stop()
        self.in3_pin.stop()
        self.in4_pin.stop()

    def forward(self, pwm):
        """
        正转，pwm 控制速度
        """
        # ENA
        self.in1_pin.ChangeDutyCycle(pwm)
        self.in2_pin.ChangeDutyCycle(0)
        # ENB
        self.in3_pin.ChangeDutyCycle(pwm)
        self.in4_pin.ChangeDutyCycle(0)

    def reverse(self, pwm):
        """
        反转，pwm 控制速度
        """
        # ENA
        self.in1_pin.ChangeDutyCycle(0)
        self.in2_pin.ChangeDutyCycle(pwm)
        # ENB
        self.in3_pin.ChangeDutyCycle(0)
        self.in4_pin.ChangeDutyCycle(pwm)

    def turn_left(self, pwm):
        """
        左转
        """
        # ENA
        self.in1_pin.ChangeDutyCycle(0)
        self.in2_pin.ChangeDutyCycle(0)
        # ENB
        self.in3_pin.ChangeDutyCycle(pwm)
        self.in4_pin.ChangeDutyCycle(0)

    def turn_right(self, pwm):
        """
        右转
        """
        # ENA
        self.in1_pin.ChangeDutyCycle(pwm)
        self.in2_pin.ChangeDutyCycle(0)
        # ENB
        self.in3_pin.ChangeDutyCycle(0)
        self.in4_pin.ChangeDutyCycle(0)
