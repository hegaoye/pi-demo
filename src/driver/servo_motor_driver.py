# coding=utf-8
import atexit
import time

import RPi.GPIO as GPIO


class ServoMotorDriver(object):
    """
    舵机驱动
    """

    def __init__(self):
        atexit.register(GPIO.cleanup)
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(13, GPIO.OUT)
        self.p = GPIO.PWM(13, 50)

    def openLock(self):
        """
        开锁控制
        0.5	-90
        1.0	-45
        1.5	0
        2.0	45
        2.5	90
        """
        self.p.start(0)
        time.sleep(0.02)
        self.p.ChangeDutyCycle(2)
        time.sleep(1)
        self.p.ChangeDutyCycle(0)
        atexit.register(GPIO.cleanup)
        # time.sleep(0.2)
        # time.sleep(1)
        # self.lock()

    def lock(self):
        """
        锁定锁控制
        """
        self.p.start(0)
        time.sleep(0.02)
        self.p.ChangeDutyCycle(15)
        time.sleep(1)
        self.p.ChangeDutyCycle(0)
        time.sleep(0.2)

    # 根据输入参数类型修改占空比
    def gs90_angle(self,angle):

        if isinstance(angle, str):
            if angle.upper() == 'STOP':
                self.p.ChangeDutyCycle(0)
            else:
                print('Input invalid')
        elif isinstance(angle, int) or isinstance(angle, float):
            self.p.ChangeDutyCycle(2.5 + angle * 10 / 180)


if __name__ == "__main__":
    lockSV = ServoMotorDriver()

    while True:
        for angle in range(0, 180, 45):
            lockSV.gs90_angle(angle)
            time.sleep(0.1)
            lockSV.gs90_angle('stop')
            time.sleep(0.5)

        for angle in range(180, 0, -45):
            lockSV.gs90_angle(angle)
            time.sleep(0.1)
            lockSV.gs90_angle('stop')
            time.sleep(0.5)