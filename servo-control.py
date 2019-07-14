# -*- coding: utf-8 -*-
import Adafruit_PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685()


def set_servo_angle(channel, angle):              #输入角度转换成12^精度的数值
    date=4096*((angle*11)+500)/20000              #进行四舍五入运算 date=int(4096*((angle*11)+500)/(20000)+0.5)
    pwm.set_pwm(channel, 0,int(date))

pwm.set_pwm_freq(50)


print('Moving servo on channel x, press Ctrl-C to quit...')
while True:
    # Move servo on channel O between extremes.
    channel=int(input('pleas input channel:'))
    angle=int(input('pleas input angle:'))
    set_servo_angle(channel, angle)


    #time.sleep(1)

