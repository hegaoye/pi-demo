# coding=utf-8
import time

import RPi.GPIO as GPIO

from relay_driver import RelayDriver


class ButtonDriver(object):
    def __init__(self, pin, callback):
        self.pin = pin
        self.func = callback
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self.callback, bouncetime=200)
        # GPIO.add_event_callback(self.pin, self.callback)

    def read(self):
        """
        开灯控制
        :return:
        """
        return GPIO.input(self.pin)

    def callback(self, pin):
        if GPIO.event_detected(self.pin):
            print("检测到事件")
            print("执行回调函数")
            self.func()


def callback_test():
    print("被回调执行了")


if __name__ == '__main__':
    button = ButtonDriver(26, callback_test)
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
