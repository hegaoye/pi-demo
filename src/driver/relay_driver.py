#!/usr/bin/env python
# coding=utf-8
import time

import RPi.GPIO as GPIO


# 继电器控制类
class RelayDriver(object):
    def __init__(self, pin):
        self.pin = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

    def on(self):
        """
        开灯控制
        :return:
        """
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def off(self):
        """
        关灯控制
        :return:
        """
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.HIGH)


if __name__ == '__main__':
    light = RelayDriver(25)
    for i in range(1, 1000):
        time.sleep(0.2)
        light.on()
        time.sleep(0.2)
        light.off()
