import RPi.GPIO as GPIO

from time import sleep

ctrlpin = 12  # 指定引脚，物理引脚编号32

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # 设置引脚编号系统，BOARD指的是物理引脚命名方式
GPIO.setup(ctrlpin, GPIO.OUT)  # 设置引脚32为输出

gs90_pwm = GPIO.PWM(ctrlpin, 50)  # 创建gs90_pwm实例，并设置频率为50Hz
gs90_pwm.start(0)  # 启动gs90_pwm实例，占空比为0


# 根据输入参数类型修改占空比
def gs90_angle(angle):
    if isinstance(angle, str):
        if angle.upper() == 'STOP':
            gs90_pwm.ChangeDutyCycle(0)
        else:
            print('Input invalid')
    elif isinstance(angle, int) or isinstance(angle, float):
        gs90_pwm.ChangeDutyCycle(2.5 + angle * 10 / 180)


if __name__ == "__main__":

    while True:
        for angle in range(0, 270, 45):
            gs90_angle(angle)
            sleep(0.1)
            gs90_angle('stop')
            sleep(0.5)

        for angle in range(-45, 0, 270):
            gs90_angle(angle)
            sleep(0.1)
            gs90_angle('stop')
            sleep(0.5)
