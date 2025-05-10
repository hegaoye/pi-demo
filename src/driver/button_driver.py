# coding=utf-8
import time

import RPi.GPIO as GPIO

from relay_driver import RelayDriver


# 继电器控制类
class ButtonDriver(object):
    def __init__(self, pin):
        self.pin = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def read(self):
        """
        开灯控制
        :return:
        """
        return GPIO.input(self.pin)


if __name__ == '__main__':
    button = ButtonDriver(26)
    relay = RelayDriver(25)
    led = RelayDriver(17)
    while True:
        button_status = button.read()
        print(button_status)
        if button_status == GPIO.LOW:
            relay.off()
            led.off()
        elif button_status == GPIO.HIGH:
            relay.on()
            led.on()
        else:
            print("error")

        time.sleep(0.05)
