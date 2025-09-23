from time import sleep

import RPi.GPIO as GPIO

ENA = 15  # 指定引脚
IN1 = 4  # 指定引脚
IN2 = 14  # 指定引脚

GPIO.setmode(GPIO.BCM)  # 设置引脚编号系统，BOARD指的是物理引脚命名方式
GPIO.setup(ENA, GPIO.OUT)  # 设置引脚
GPIO.setup(IN1, GPIO.OUT)  # 设置引脚
GPIO.setup(IN2, GPIO.OUT)  # 设置引脚

ena_pin = GPIO.PWM(ENA, 50)  # 创建电机pwm实例，并设置频率为50Hz
ena_pin.start(0)

# in1_pin = GPIO.output(IN2, GPIO.LOW)
# in1_pin.start(0)
#
# in2_pin = GPIO.output(IN2, GPIO.LOW)
# in2_pin.start(0)


def forward(pwm=50):
    ena_pin.ChangeDutyCycle(pwm)
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)


def reverse(pwm=50):
    ena_pin.ChangeDutyCycle(pwm)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)


def stop():
    # in1_pin.stop()
    # in2_pin.stop()
    ena_pin.ChangeDutyCycle(0)
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)


if __name__ == '__main__':
    # forward(50)
    # sleep(1)
    for pwm in range(35, 100):
        forward(pwm)
        sleep(.2)

    for pwm in range(35, 100):
        reverse(pwm)
        sleep(.1)

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
