# ElementaryAdditionAuxiliaryProgram (小学一年级加法辅助程序)
# Powered by RMSHE / 2022.09.22
# GitHub Open Source: https://github.com/RMSHE-MSH/Python-Homework-Open-Source-Project
from random import *


# 这里定义10以内的加法为两个或多个正整数加和后的结果<=10;
# 生成加和<=10的多项式;
def PolynomialGenerate():
    while True:
        SUM = 0
        Formula_Str = ""
        Polynomial = []  # 列表数据可能留存备用(返回列表数据可以记录用于判断是否重复,不过我这里不做该判断);
        for i in range(randint(2, 32)):  # 生成的多项式最少为2项;
            Polynomial.append(randint(0, 10))  # 10以内小学生计算题应该不涉及浮点数,故这里只伪随机生成整形值;
            Formula_Str = Formula_Str + " + " + str(Polynomial[i])  # 格式化为多项式字符串;
            SUM = Polynomial[i] + SUM  # 计算答案;

        # 判断加和是否<=10;
        if SUM <= 10:
            break

    return Formula_Str[2:] + " = ", Polynomial, SUM


Count = [0, 0]  # 缓存正确数与错误数;
print("Stop answering questions after typing \"STOP\".")
while True:
    _Polynomial = PolynomialGenerate()  # 生成加和<=10的多项式;
    print("Please calculate this formula and fill in your answer: ", _Polynomial[0])  # 打印题目;
    INPUT = input()  # 等待输入答案;
    if INPUT == "STOP":  # 如果输入"STOP"则,统计 答题总数,正确数量, 正确率 后退出程序;
        break
    elif INPUT == str(_Polynomial[2]):
        Count[0] += 1  # 对题数加一;
        print("Correct answer.")  # 回答正确;
    else:
        Count[1] += 1  # 错题数加一;
        print("Wrong answer. The correct answer is: ", _Polynomial[2])  # 回答错误,打印正确答案;

# 打印统计结果;
print("Total:", Count[0] + Count[1], "\tCorrect:", Count[0], "\tCorrectRate:", '%.2f' % (Count[0] / (Count[0] + Count[1])))
