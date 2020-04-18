import math
from math import fabs
from math import pi
import random

def cot_se_p(angle):
    x = (angle/180)*pi;
    x1 = float(x)
    x2 = float(x)
    g = 0
    t = x1
    n = 1
    while (fabs(t) >= 1e-10):
        g += t
        n += 1
        t = -t * x1 * x1 / (2 * n - 1) / (2 * n - 2)   #sin

    cosTotal  = 1
    count = 2
    term = 1
    #x=float(x)
    while abs(term) > 1e-20:
        term *= (-x2 * x2)/( count * (count-1) )
        cosTotal += term
        count += 2                                   #cos
        #print("%1d  %22.17e" % (count, term))
    g = cosTotal/g
    return g


def test_cot():
    num = 1000
    test_number = [0] * num
    sum = 0
    flag = 0  # 判断误差是否大于0.001的标志，默认为0，小于0.001
    for i in range(num):  # 随机选择1000个随机数
        test_number[i] = random.uniform(0, 360)
    for i in range(num):
        sta_val = 1 / math.tan(test_number[i] / 180 * pi)  # 标准值
        tes_val = cot_se_p(test_number[i])  # 需要测试的值
        error = abs(sta_val - tes_val)  # 误差
        if error > 0.001:
            flag = 1
            tes_val = 1 / math.tan(test_number[i] / 180 * pi)
            error = abs(sta_val - tes_val)
            if error <= 0.001:
                flag = 0
        sum = sum + error
    avgError = sum / num  # 平均误差
    return flag, avgError


if __name__ == '__main__':
    flag, avgError = test_cot()
    print('flag = ', flag)
    print('avgError = ', avgError)