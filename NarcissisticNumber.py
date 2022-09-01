import math


def NarcissisticNumberJudge(num):
    isNarcissisticNumberJudge = False
    result = 0
    for i in range(len(str(num))):
        result = int(result + math.pow(int(str(num)[i]), len(str(num))))
        if result == num and result != 0:
            isNarcissisticNumberJudge = True
    return isNarcissisticNumberJudge


k = 0
while True:
    if NarcissisticNumberJudge(k):
        print(k)
    k += 1
