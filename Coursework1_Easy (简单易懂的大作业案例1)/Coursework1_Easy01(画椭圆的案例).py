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

MP.initgraph(800, 800)  # 初始化窗口和画布(画布中心点的坐标是:(400,400));

# i将从0开始逐步增加到360,步长为8;
for i in range(0, 360, 8):
    Color = MPCS.HSV(i, 0.6, 0.7)  # 使颜色发生渐变(色相值随i不断增加,饱和度值固定为0.6,明度值固定为0.7);
    pencolor(Color)  # 设置画笔颜色;

    # 画椭圆[椭圆外切矩形左上角点坐标为:(100,100),右下角点的坐标为:(700,300). 旋转中心坐标在:(400,400),旋转角度随i不断增加];
    MP.ellipse(100, 100, 700, 300, i, 400, 400)

MP.EndBatchDraw()  # 结束批量绘图;
done()  # 绘图结束;
