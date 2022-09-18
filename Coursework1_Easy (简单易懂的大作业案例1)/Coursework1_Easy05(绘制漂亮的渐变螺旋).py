"""------------------------------------------------------------------------------------------------------------
# 运行本程序前请先安装 MountPenglai 0.0.3
# 安装方法: pip install MountPenglai
# 注意: 不推荐使用镜像站安装,可能会出问题(当然也可能没有问题,主要是我没试过镜像,Pipy服务器在国外,如果嫌慢的话可以使用魔法)
# MountPenglai 已经包含 turtle 了,这里只需导入一个包即可
# Pipy链接: https://pypi.org/project/MountPenglai/
# GitHub链接: https://github.com/RMSHE-MSH/Python-Homework-Open-Source-Project

MountPenglai 是由我(RMSHE)编写的 turtle库 功能增强包,旨在改变turtle的绘图逻辑,使之参数化.
当然我也增加了很多turtle本身内置函数无法实现的功能,在 参数化绘图、旋转、色彩变换 上非常方便.

# Powered by RMSHE / 2022.09.17
------------------------------------------------------------------------------------------------------------"""
from MountPenglai import *  # 从包中导入所有类;

MP = MountPenglai()
MPCS = MPColorSystem()

MP.BeginBatchDraw()  # 开始批量绘图;

MP.initgraph(900, 900)  # 初始化窗口和画布(画布中心点的坐标是:(450,450));

# 程序执行速度较慢,运行后需等待一定时间;
position = []
i = 0
j = 0
H = 0
while i < 250:
    # 计算阿基米德螺旋线;
    x = 450 + int((1 + j * i) * sin(i))
    y = 450 + int((1 + j * i) * cos(i))

    # 将螺旋线离散点坐标存入数组position;
    position.append(x)
    position.append(y)

    fillcolor(MPCS.HSV(H, j / 2, 0.8))  # 色彩渐变;
    MP.solidcircle(x, y, j * 4)  # 绘制渐变的圆;

    i += 0.1
    j += 0.0007
    if H > 360:
        H = 0
    H += 1

MP.polyline(position)  # 绘制多条连续的线;

MP.EndBatchDraw()  # 结束批量绘图;
done()  # 绘图结束;
