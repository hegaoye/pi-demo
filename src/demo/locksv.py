#!/usr/bin/env python
# coding=utf-8
import atexit
import time

import RPi.GPIO as GPIO


class LockSV(object):
    def __init__(self):
        atexit.register(GPIO.cleanup)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12, GPIO.OUT, initial=False)
        self.pwm = GPIO.PWM(12, 50)

    def openLock(self):
        self.pwm.start(0)
        time.sleep(0.2)
        # 0.5ms + 角度 * (2ms/180)
        #2 ~ 13
        self.pwm.ChangeDutyCycle(2.8 + 180 * 10 / 180)
        # self.pwm.ChangeDutyCycle(2)
        time.sleep(1)
        # self.pwm.stop(0)
        self.pwm.ChangeDutyCycle(0)
        # time.sleep(0.2)

    def lock(self):
        self.pwm.start(0)
        time.sleep(0.2)
        self.pwm.ChangeDutyCycle(15)
        time.sleep(1)
        self.pwm.ChangeDutyCycle(0)
        time.sleep(0.2)


if __name__ == "__main__":
    lockSV = LockSV()
    lockSV.openLock()
    # time.sleep(1)
    # lockSV.lock()
