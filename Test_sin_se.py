import math
import random
from math import fabs
from math import pi

def sin_se_p(angle):
    x = (angle/180)*pi;
    g = 0
    t = x
    n = 1
    while (fabs(t) >= 1e-10):
        g += t
        n += 1
        t = -t * x * x / (2 * n - 1) / (2 * n - 2)
    return g


def test_sin():
    num = 1000
    test_number = [0] * num
    sum = 0
    flag = 0  # 判断误差是否大于0.001的标志，默认为0，小于0.001
    for i in range(num):  # 随机选择1000个随机数
        test_number[i] = random.uniform(0, 360)
    for i in range(num):
        sta_val = math.sin(test_number[i] / 180 * pi)  # 标准值
        tes_val = sin_se_p(test_number[i])  # 需要测试的值
        error = abs(sta_val - tes_val)  # 误差
        if error > 0.001:
            flag = 1
            tes_val = math.sin(test_number[i] / 180 * pi)
            error = abs(sta_val - tes_val)
            if error <= 0.001:
                flag = 0
        sum = sum + error
    avgError = sum / num  # 平均误差
    return flag, avgError


if __name__ == '__main__':
    flag, avgError = test_sin()
    print('flag = ', flag)
    print('avgError = ', avgError)