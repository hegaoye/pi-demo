from time import sleep

import RPi.GPIO as GPIO


if __name__ == '__main__':
    ENA = 5  # 指定引脚
    IN1 = 6  # 指定引脚
    IN2 = 13  # 指定引脚

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

    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    ena_pin.ChangeDutyCycle(50)

    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    enb_pin.ChangeDutyCycle(50)

    sleep(10)
