# coding=utf-8
from time import sleep
import RPi.GPIO as GPIO


class ServoDriver(object):
    """
    舵机驱动
    """

    def __init__(self, pin, total_angle=180):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)  # 设置引脚编号系统，BOARD指的是物理引脚命名方式
        GPIO.setup(pin, GPIO.OUT)  # 设置引脚32为输出
        self.total_angle = total_angle  # 总度数 默认180度
        self.pwm = GPIO.PWM(pin, 50)  # 创建舵机pwm实例，并设置频率为50Hz

    def angle(self, angle):
        """
        根据输入参数类型修改占空比
        高电平持续时间/ms	舵机旋转角度/°
            0.5	          -90
            1.0	          -45
            1.5	          0
            2.0	          45
            2.5	          90
        :param angle: 角度
        """
        # 角度控制脉冲范围 2ms ~ 13ms 180度 经验值 2.5ms 或 2.8ms 为 0度，13为180度
        # 脉冲公式= 2.5ms + 角度 * 10 / 总度数
        self.pwm.ChangeDutyCycle(2.5 + angle * 10 / self.total_angle)
        # 关键的休眠 1s 充分执行
        sleep(1)

    def start(self):
        """
        开始
        """
        self.pwm.start(0)

    def stop(self):
        """
        停止
        """
        self.pwm.stop()

    def pause(self):
        """
        暂停，悬停
        """
        self.pwm.ChangeDutyCycle(0)


if __name__ == '__main__':
    servo = ServoDriver(12)
    servo.start()
    servo.angle(0)
    sleep(1)
    servo.pause()
    sleep(1)
    servo.angle(90)
    sleep(1)
    servo.pause()
    sleep(0.5)
    servo.stop()
