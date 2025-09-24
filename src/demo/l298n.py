from time import sleep

import RPi.GPIO as GPIO

ENA = 15  # 指定引脚
IN1 = 4  # 指定引脚
IN2 = 14  # 指定引脚

ENB = 24
IN3 = 22
IN4 = 23

GPIO.setmode(GPIO.BCM)  # 设置引脚编号系统，BOARD指的是物理引脚命名方式
GPIO.setup(ENA, GPIO.OUT)  # 设置引脚
GPIO.setup(IN1, GPIO.OUT)  # 设置引脚
GPIO.setup(IN2, GPIO.OUT)  # 设置引脚

GPIO.setup(ENB, GPIO.OUT)  # 设置引脚
GPIO.setup(IN3, GPIO.OUT)  # 设置引脚
GPIO.setup(IN4, GPIO.OUT)  # 设置引脚

ena_pin = GPIO.PWM(ENA, 100)  # 创建电机pwm实例，并设置频率为50Hz
ena_pin.start(0)
enb_pin = GPIO.PWM(ENB, 100)  # 创建电机pwm实例，并设置频率为50Hz
enb_pin.start(0)


def forward(pwm=50):
    enb_pin.ChangeDutyCycle(pwm)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

    ena_pin.ChangeDutyCycle(pwm)
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)


def reverse(pwm=50):
    enb_pin.ChangeDutyCycle(pwm)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

    ena_pin.ChangeDutyCycle(pwm)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)


def left(pwm=50):
    enb_pin.ChangeDutyCycle(pwm)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

    ena_pin.ChangeDutyCycle(pwm)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)


def right(pwm=50):
    enb_pin.ChangeDutyCycle(pwm)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

    ena_pin.ChangeDutyCycle(pwm)
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)


def stop():
    ena_pin.stop()
    enb_pin.stop()
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)


if __name__ == '__main__':
    forward(100)
    sleep(10)
    reverse(100)
    sleep(10)
    left(100)
    sleep(10)
    right(100)
    sleep(10)
    # for pwm in range(35, 100):
    #     forward(pwm)
    #     sleep(.1)
    #
    # for pwm in range(35, 100):
    #     reverse(pwm)
    #     sleep(.1)

    stop()
    # while True:
    #     for pwm in range(100):
    #         forward(pwm)
    #         sleep(.2)
    #
    #     reverse()
    #     sleep(5)
    #     forward()
    #     sleep(.3)
    #     stop()
    #     sleep(1)
