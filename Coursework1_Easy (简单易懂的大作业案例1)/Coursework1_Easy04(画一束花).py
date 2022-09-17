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
# 程序名称：一束漂亮的花
# 绘图作者：yangw80 <yw80@qq.com>
------------------------------------------------------------------------------------------------------------"""

from MountPenglai import *  # 从包中导入所有类;

MP = MountPenglai()
MPCS = MPColorSystem()


# 画花朵;
def flower(x, y, color):
    pencolor(color)
    d = 15
    for a in range(0, 360):
        e = d * (1 + sin(pi / 180 * a * 5))
        x1 = int(x + e * cos(pi / 180 * a))
        y1 = int(y + e * sin(pi / 180 * a))
        x2 = int(x + e * cos(pi / 180 * a + pi / 5))
        y2 = int(y + e * sin(pi / 180 * a + pi / 5))
        MP.line(x1, y1, x2, y2)
    pass


# 画蝴蝶结;
def tie(x, y, color):
    pencolor(color)
    d = 80
    for a in range(0, 360):
        e = d * (1 + sin(pi / 180 * a * 4))
        x1 = int(x + e * cos(pi / 180 * a))
        y1 = int(y + e * sin(pi / 180 * a) / 2)
        x2 = int(x + e * cos(pi / 180 * a + pi / 9))
        y2 = int(y + e * sin(pi / 180 * a + pi / 9) / 4.5)
        MP.line(x1, y1, x2, y2)
    pass


MP.BeginBatchDraw()  # 开始批量绘图;
MP.initgraph(800, 800)  # 初始化窗口和画布(画布中心点的坐标是:(400,400));

# 画枝干;
pencolor("GREEN")
MP.line(189, 372, 180, 400)
MP.line(310, 160, 325, 68)
MP.line(310, 160, 187, 374)
MP.line(150, 140, 189, 374)
MP.line(430, 176, 190, 374)
MP.line(370, 110, 187, 374)
MP.line(250, 72, 189, 372)
MP.line(253, 192, 190, 374)
MP.line(189, 372, 187, 400)
MP.line(189, 372, 182, 400)
MP.line(189, 372, 200, 120)

# 画花朵;
flower(320, 160, "RED")
flower(200, 120, "YELLOW")
flower(150, 140, MPCS.RGB(255, 107, 129))
flower(430, 176, MPCS.RGB(255, 127, 0))
flower(370, 110, MPCS.RGB(239, 179, 52))
flower(250, 72, MPCS.RGB(235, 95, 186))
flower(325, 68, MPCS.RGB(228, 119, 98))
flower(253, 190, MPCS.RGB(247, 169, 117))

# 画蝴蝶结;
tie(195, 354, "#fd79a8")

MP.EndBatchDraw()  # 结束批量绘图;
done()  # 绘图结束;
