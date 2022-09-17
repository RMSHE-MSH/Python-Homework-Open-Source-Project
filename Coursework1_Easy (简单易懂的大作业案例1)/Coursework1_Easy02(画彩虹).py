# 运行本程序前请先安装 MountPenglai 0.0.3
# 安装方法: pip install MountPenglai
# 注意: 不推荐使用镜像站安装,可能会出问题(当然也可能没有问题,主要是我没试过镜像,Pipy服务器在国外,如果嫌慢的话可以使用魔法)
# MountPenglai 已经包含 turtle 了,这里只需导入一个包即可
# Pipy链接: https://pypi.org/project/MountPenglai/
# GitHub链接: https://github.com/RMSHE-MSH/Python-Homework-Open-Source-Project

"""--------------------------------------------------------------------------------
MountPenglai 是由我(RMSHE)编写的 turtle库 功能增强包,旨在改变turtle的绘图逻辑,使之参数化.
当然我也增加了很多turtle本身内置函数无法实现的功能,在 参数化绘图、旋转、色彩变换 上非常方便.
--------------------------------------------------------------------------------"""
# Powered by RMSHE / 2022.09.17

from MountPenglai import *  # 从包中导入所有类;

MP = MountPenglai()
MPCS = MPColorSystem()

MP.BeginBatchDraw()  # 开始批量绘图;

MP.initgraph(640, 480)  # 初始化窗口和画布(画布中心点的坐标是:(400,400));

# 画渐变的天空(通过亮度逐渐增加);
L = 0.5  # 设置天空初始亮度为0.5;
pensize(4)  # 设置线宽为 4;
for i in range(0, 480, 4):
    Color = MPCS.HSV(190, 1, L)  # 色相为190,饱和度为1,亮度逐渐增加;
    L += 0.004166667  # 亮度逐渐增加;
    pencolor(Color)  # 设置画笔颜色;

    MP.line(0, i, 800, i)  # 画线(颜色不断渐变);

# 画彩虹(通过色相逐渐增加);
H = 0  # 设置彩虹初始色相为0;
pensize(2)  # 设置线宽为 2;
for r in range(344, 400):
    Color = MPCS.HSV(H, 0.7, 0.8)  # 色相逐渐增加,饱和度为0.7,亮度为0.8;
    H += 5  # 色相逐渐增加;
    pencolor(Color)  # 设置画笔颜色;

    MP.Circle(500, 480, r)  # 画圆(画彩虹);

MP.EndBatchDraw()  # 结束批量绘图;
done()  # 绘图结束;
