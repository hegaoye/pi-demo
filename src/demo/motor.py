import RPi.GPIO as GPIO

from time import sleep

IN1 = 14  # 指定引脚
IN2 = 15  # 指定引脚

GPIO.setmode(GPIO.BCM)  # 设置引脚编号系统，BOARD指的是物理引脚命名方式
GPIO.setup(IN1, GPIO.OUT)  # 设置引脚
GPIO.setup(IN2, GPIO.OUT)  # 设置引脚

in1_pwm = GPIO.PWM(IN1, 50)
in1_pwm.start(0)

in2_pwm = GPIO.PWM(IN2, 50)
in2_pwm.start(0)


def forward(pwm=50):
    in1_pwm.start(pwm)
    in2_pwm.start(0)
    # GPIO.output(IN1, GPIO.HIGH)
    # GPIO.output(IN2, GPIO.LOW)


def reverse(pwm=50):
    in1_pwm.start(0)
    in2_pwm.start(pwm)
    # GPIO.output(IN1, GPIO.LOW)
    # GPIO.output(IN2, GPIO.HIGH)


def stop():
    in1_pwm.start(0)
    in2_pwm.start(0)
    # GPIO.output(IN1, False)
    # GPIO.output(IN2, False)


if __name__ == '__main__':
    for pwm in range(30, 100):
        forward(pwm)
        sleep(.1)

    for pwm in range(30, 100):
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
