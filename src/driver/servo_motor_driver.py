#!/usr/bin/env python
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
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(14, GPIO.OUT, initial=False)
        self.p = GPIO.PWM(14, 50)

    def openLock(self):
        """
        开锁控制
        """

        self.p.start(0)
        time.sleep(0.02)
        self.p.ChangeDutyCycle(2)
        time.sleep(1)
        self.p.ChangeDutyCycle(0)
        time.sleep(0.2)
        time.sleep(1)
        self.lock()

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


if __name__ == "__main__":
    lockSV = ServoMotorDriver()
    lockSV.openLock()
