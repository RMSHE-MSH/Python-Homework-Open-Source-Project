# FastPowerProgressbar(加速度进度条)
# Powered by RMSHE / 2022.09.29
# GitHub Open Source: https://github.com/RMSHE-MSH/Python-Homework-Open-Source-Project
# 警告: 本代码 ".py" Python文件必须以 UTF-8 编码保存,否则进度条字符可能会输出乱码!
from time import *

# 这是较为通用的代码形式;
"""---------------------------------------------------------------------------------------------------------------------------
# 这是骗人的FastPower函数;
def FastPower(Pos, Zoom=100, NUMmax=100, n=8):
    return int(Zoom * pow((Pos / NUMmax) + 0.5 * (1 - (Pos / NUMmax)), n))


# 做区间映射,将[Omin，Omax]上每个数映射到区间[Nmin,Nmax]上;
def IntervalMapping(Pos, Omax=100, Omin=0, Nmax=100, Nmin=0):
    return (Nmax - Nmin) / (Omax - Omin) * (Pos - Omin) + Nmin


# 文本进度条(进度条位置,进度条规模);
def Bar(Pos=0, scale=100):
    start = perf_counter()  # 获取起始时间;
    # 显示进度;
    print("\r{:^3.0f}% / {:.2f}s\t|{}{}|".format(IntervalMapping(Pos, scale), perf_counter() - start, "█" * FastPower(IntervalMapping(Pos, scale)),
                                                 " " * (100 - FastPower(IntervalMapping(i, scale)))), end="")
    sleep(0.05)


# 测试;
for i in range(101):
    Bar(i)
---------------------------------------------------------------------------------------------------------------------------"""

# 这是作业特化的代码形式;
start = perf_counter()
for i in range(101):
    FastPowerValue = int(100 * pow(i * 0.01 + 0.5 * (1 - i * 0.01), 8))  # FastPower函数;
    print("\r{:^3.0f}% / {:.2f}s\t|{}{}|".format(i, perf_counter() - start, "█" * FastPowerValue, " " * (100 - FastPowerValue)), end="")
    sleep(0.05)

# format函数中第一项为进度条当前进度,第二项为当前所用时间,第三项为打印FastPowerValue个"█"字符,第四项为打印(100 - FastPowerValue)个"space"字符;
# 其中 (100 - FastPowerValue) + FastPowerValue = 100;
