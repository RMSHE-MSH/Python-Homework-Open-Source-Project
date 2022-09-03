# Powered by RMSHE; 20220901;
import math


# 此函数用来判断给定的数是否是自幂数;
def NarcissisticNumberJudge(num):
    isNarcissisticNumber = False
    result = 0
    for i in range(len(str(num))):
        result = int(result + math.pow(int(str(num)[i]), len(str(num))))
        if result == num:
            isNarcissisticNumber = True
    return isNarcissisticNumber


# 一个固定的进制中，一个n位自然数等于自身各个数位上数字的n次幂之和，则称此数为自幂数;

k = 0
while True:
    if NarcissisticNumberJudge(k):
        print(k)
    k += 1
