# coding=utf-8
from time import sleep
import RPi.GPIO as GPIO


class MotorDriver(object):
    """
    舵机驱动
    """

    def __init__(self, pin1,pin2, total_angle=180):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)  # 设置引脚编号系统，BOARD指的是物理引脚命名方式
        GPIO.setup(pin1, GPIO.OUT)  # 设置引脚
        GPIO.setup(pin2, GPIO.OUT)  # 设置引脚
        self.total_angle = total_angle  # 总度数 默认180度
        self.pwm = GPIO.PWM(pin1, 50)  # 创建舵机pwm实例，并设置频率为50Hz
        self.pwm = GPIO.PWM(pin2, 50)  # 创建舵机pwm实例，并设置频率为50Hz

    def start(self):
        """
        开始
        """
        self.pwm.start(0)

    def stop(self):
        """
        停止
        """
        self.pwm.stop()

    def pause(self):
        """
        暂停，悬停
        """
        self.pwm.ChangeDutyCycle(0)


if __name__ == '__main__':
    servo = MotorDriver(12)
    servo.start()
    servo.angle(0)
    sleep(1)
    servo.pause()
    sleep(1)
    servo.angle(90)
    sleep(1)
    servo.pause()
    sleep(0.5)
    servo.stop()
