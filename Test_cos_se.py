#  -*-coding:utf8;-*-
#  qpy:3
#  qpy:console
import math
import random
from math import pi


def fa(a):
    b=1
    while a!=1:
        b*=a
        a-=1
    return b

def taylor(x,n):
    a=1
    count=1
    for k in range(1, n):
        if count%2!=0:
            a-=(x**(2*k))/fa(2*k)
        else:
            a+=(x**(2*k))/fa(2*k)
        count+=1
    return a

def cos_se(x):
    x = (x/180)*math.pi
    return taylor(x, 10)


def test_cos():
    num = 1000
    test_number = [0] * num
    sum = 0
    flag = 0  # 判断误差是否大于0.001的标志，默认为0，小于0.001
    for i in range(num):  # 随机选择1000个随机数
        test_number[i] = random.uniform(0, 360)
    for i in range(num):
        sta_val = math.cos(test_number[i] / 180 * pi)  # 标准值
        tes_val = cos_se(test_number[i])  # 需要测试的值
        error = abs(sta_val - tes_val)  # 误差
        if error > 0.001:
            flag = 1
            tes_val = math.cos(test_number[i] / 180 * pi)
            error = abs(sta_val - tes_val)
            if error <= 0.001:
                flag = 0
        sum = sum + error
    avgError = sum / num  # 平均误差
    return flag, avgError


if __name__ == '__main__':
    flag, avgError = test_cos()
    print('flag = ', flag)
    print('avgError = ', avgError)
