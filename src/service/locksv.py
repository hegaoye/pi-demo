#!/usr/bin/env python
# coding=utf-8
import atexit
import time

import RPi.GPIO as GPIO


class LockSV(object):
    def __init__(self):
        atexit.register(GPIO.cleanup)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(14, GPIO.OUT, initial=False)
        self.p = GPIO.PWM(14, 50)
        self.stateObj = State()

    def openLock(self):
        '''
        开锁控制
        '''
        state = self.stateObj.read()
        if state == 'open':
            return

        self.p.start(0)
        time.sleep(0.02)
        self.p.ChangeDutyCycle(2)
        time.sleep(1)
        self.p.ChangeDutyCycle(0)
        time.sleep(0.2)
        self.stateObj.write('open')
        time.sleep(1)
        self.lock()

    def lock(self):
        '''
        锁定锁控制
        '''
        state = self.stateObj.read()

        if state == 'lock':
            return
        self.p.start(0)
        time.sleep(0.02)
        self.p.ChangeDutyCycle(15)
        time.sleep(1)
        self.p.ChangeDutyCycle(0)
        time.sleep(0.2)
        self.stateObj.write('lock')


if __name__ == "__main__":
    lockSV = LockSV()
    lockSV.openLock()
