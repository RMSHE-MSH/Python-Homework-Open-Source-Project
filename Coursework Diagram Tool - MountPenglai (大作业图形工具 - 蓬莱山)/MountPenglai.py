'''-------------------------------------------------
Powered by RMSHE / 2022.09.08;

将 turtle 的绘图逻辑更改为 Organ-Field GUI 样式;
Organ-Field GUI 的绘图逻辑我参考的是 AutoCAD;
turtle 的使用逻辑过于直观,因此造成了使用不便,翻了一遍文档,
还好基础该有的都有,我要重新将它封装成C++图形库的使用逻辑;

项目代号: 蓬莱山(MountPenglai) / 生命周期: 一个月;
我就是要用英文写注释,咬我呀 ^_~
--------------------------------------------------'''
from turtle import *
from math import *
import _thread


class MountPenglai:
    canvwidth = None
    canvheight = None

    # Initialize the canvas;
    def initialize(self, width, height, BGcolor=None):
        screensize(width, height)
        speed("fastest")
        hideturtle()
        self.canvwidth = width
        self.canvheight = height

        if BGcolor == None:
            bgcolor("#282c34")
        else:
            bgcolor(BGcolor)

        pencolor("#54575c")
        fillcolor("#70a1ff")
        pass

    # 进行伽利略变换: 将画布原点定在窗口中央是不合适的,一旦涉及到坐标的矩阵变换(特别是旋转)时就要考虑正负,这很麻烦;
    # 应该将原点设在窗口左上角,并且把Y轴方向反转,使其向下为正向,X轴向右为正向.这样整个可用绘图空间都在一个象限内;
    # Perform GalileanTransformation: It is inappropriate to set the origin of the canvas in the center of the window.
    # Once it involves the matrix transformation of coordinates (especially rotation), it is very troublesome to consider the positive and negative;
    def GalileanTransformation(self, x, y):
        x = x - 0.5 * self.canvwidth
        y = -(y - 0.5 * self.canvheight)
        return x, y

    # 指定点绕基点旋转(待旋转的点的坐标,基点坐标,旋转角度);
    # RMSHE built-in tool [rotation matrix for 2D plane];
    def RotationMatrix(self, x, y, xbase, ybase, angle):
        Rx = (x - xbase) * cos(pi / 180.0 * angle) - (y - ybase) * sin(pi / 180.0 * angle) + xbase
        Ry = (x - xbase) * sin(pi / 180.0 * angle) + (y - ybase) * cos(pi / 180.0 * angle) + ybase
        return Rx, Ry

    # 将画笔传送到指定位置;
    # Teleport the pen to the specified location;
    def teleport(self, x, y):
        Point = self.GalileanTransformation(x, y)
        penup()
        setposition(Point[0], Point[1])
        pendown()
        pass

    # 画点(点的坐标,点的视觉半径)
    # draw dots;
    def putpixel(self, x, y, radius=0.5):
        self.teleport(x, y + radius)

        pencolor(fillcolor())
        width(0)
        begin_fill()
        circle(radius)
        end_fill()
        pass

    # 画一条线段(两点坐标);
    # draw straight lines(Two points define a line segment);
    def line(self, x0, y0, x1, y1):
        self.teleport(x0, y0)
        setposition(self.GalileanTransformation(x1, y1))
        pass

    # 画连续的多条线段(控制点列表);
    # Draw multiple consecutive line segments;
    def polyline(self, POINTs=None):
        if POINTs is None:
            return "POINTs cannot be NULL"
        elif int(len(POINTs) / 2) - 1 <= 0:
            return "The number of POINTs must be greater than one"

        i = 0
        j = 0
        while True:
            self.line(POINTs[i], POINTs[i + 1], POINTs[i + 2], POINTs[i + 3])

            j += 1
            if j == int(len(POINTs) / 2) - 1:
                break
            i += 2

        pass

    # 画无填充矩形;
    # draw unfilled rectangle(Specify the coordinates of the four vertices of the rectangle, Rotation angle, Rotation base point);
    def rectangle(self, left, top, right, bottom, angle=0, xbase=None, ybase=None):
        if angle != 0:
            if xbase is None and ybase is None:
                xbase = int((right - left) / 2) + left
                ybase = int((bottom - top) / 2) + top

            RotationResult0 = self.RotationMatrix(left, top, xbase, ybase, angle)
            RotationResult1 = self.RotationMatrix(left, bottom, xbase, ybase, angle)

            RotationResult2 = self.RotationMatrix(right, bottom, xbase, ybase, angle)
            RotationResult3 = self.RotationMatrix(right, top, xbase, ybase, angle)

            self.line(RotationResult0[0], RotationResult0[1], RotationResult1[0], RotationResult1[1])
            self.line(RotationResult1[0], RotationResult1[1], RotationResult2[0], RotationResult2[1])
            self.line(RotationResult2[0], RotationResult2[1], RotationResult3[0], RotationResult3[1])
            self.line(RotationResult3[0], RotationResult3[1], RotationResult0[0], RotationResult0[1])
        else:
            self.line(left, top, left, bottom)
            self.line(left, bottom, right, bottom)
            self.line(right, bottom, right, top)
            self.line(right, top, left, top)
        pass

    # 画无边框的填充矩形;
    # draw a Solid-rectangle;
    def solidrectangle(self, left, top, right, bottom, angle=0, xbase=None, ybase=None):
        pencolor(fillcolor())
        width(0)
        begin_fill()
        self.rectangle(left, top, right, bottom, angle, xbase, ybase)
        end_fill()
        pass

    # 画有边框的填充矩形;
    # Draw a Fill-rectangle;
    def fillrectangle(self, left, top, right, bottom, angle=0, xbase=None, ybase=None):
        begin_fill()
        self.rectangle(left, top, right, bottom, angle, xbase, ybase)
        end_fill()
        pass

    # 画无填充多边形(指定外切圆圆心坐标,指定外切圆半径,指定多边形边数,图形旋转角度,旋转基点坐标);
    # Draw a polygon,This function is very widespread, it can create polygons with any number of sides and any rotation angle in any position.
    def polygon(self, x, y, radius, steps=72, angle=0, xbase=None, ybase=None):
        if xbase is None and ybase is None:
            xbase = x
            ybase = y

        CurrentPoint = []
        i = 0
        j = 0.0
        k = 0
        while True:
            RotationResult = self.RotationMatrix(radius * cos(pi / 180.0 * j) + x, radius * sin(pi / 180.0 * j) + y, xbase, ybase, angle)
            CurrentPoint.append(int(RotationResult[0]))
            CurrentPoint.append(int(RotationResult[1]))

            i += 1
            j += 360 / steps
            if i >= steps:
                break
            k += 2

        CurrentPoint.append(CurrentPoint[0])
        CurrentPoint.append(CurrentPoint[1])
        self.polyline(CurrentPoint)

        pass

    # 画无边框的填充多边形(指定外切圆圆心坐标,指定外切圆半径,指定多边形边数,图形旋转角度,旋转基点坐标);
    # Draw a Solid-polygon,This function is very widespread, it can create polygons with any number of sides and any rotation angle in any position.
    def solidpolygon(self, x, y, radius, steps=72, angle=0, xbase=None, ybase=None):
        pencolor(fillcolor())
        width(0)
        begin_fill()

        self.polygon(x, y, radius, steps, angle, xbase, ybase)

        end_fill()
        pass

    # 画有边框的填充多边形(指定外切圆圆心坐标,指定外切圆半径,指定多边形边数,图形旋转角度,旋转基点坐标);
    # Draw a Fill-polygon,This function is very widespread, it can create polygons with any number of sides and any rotation angle in any position.
    def fillpolygon(self, x, y, radius, steps=72, angle=0, xbase=None, ybase=None):
        begin_fill()

        self.polygon(x, y, radius, steps, angle, xbase, ybase)

        end_fill()
        pass

    EllipsePoints = []  # Temporary storage list of ellipse discrete points;
    EllipseEngineState = [False, False]  # List of thread state flags for ellipse calculate;

    # Ellipse calculate 'X' Thread;
    def EllipseXEngine(self, a, c, d, steps):
        j = 0
        for i in range(0, 361, steps):
            self.EllipsePoints.insert(j, a * cos(c * i) + d)
            j += 2
        self.EllipseEngineState[0] = True
        pass

    # Ellipse calculate 'Y' Thread;
    def EllipseYEngine(self, b, c, e, steps):
        j = 1
        for i in range(0, 361, steps):
            self.EllipsePoints.insert(j, b * sin(c * i) + e)
            j += 2
        self.EllipseEngineState[1] = True
        pass

    # 画无填充的椭圆(椭圆外切矩形的左上角 x 坐标,椭圆外切矩形的左上角 y 坐标,椭圆外切矩形的右下角 x 坐标,椭圆外切矩形的右下角 y 坐标,旋转角度,旋转基点,绘图计算精度);
    # draw an unfilled ellipse(Specifies the rectangle circumscribing the ellipse);
    def ellipse(self, left, top, right, bottom, angle=0, xbase=None, ybase=None, steps=6):
        a = (right - left) / 2
        b = (bottom - top) / 2
        c = pi / 180
        d = left + a
        e = top + b

        _thread.start_new_thread(self.EllipseXEngine, (a, c, d, steps))
        _thread.start_new_thread(self.EllipseYEngine, (b, c, e, steps))

        while True:
            if self.EllipseEngineState[0] == True and self.EllipseEngineState[1] == True:
                break

        if angle != 0:
            EllipsePointsTransform = []
            if xbase is None and ybase is None:
                if xbase is None and ybase is None:
                    xbase = int((right - left) / 2) + left
                    ybase = int((bottom - top) / 2) + top

            for i in range(0, len(self.EllipsePoints), 2):
                EllipsePointsTransformTemp = self.RotationMatrix(self.EllipsePoints[i], self.EllipsePoints[i + 1], xbase, ybase, angle)
                EllipsePointsTransform.append(EllipsePointsTransformTemp[0])
                EllipsePointsTransform.append(EllipsePointsTransformTemp[1])

            self.polyline(EllipsePointsTransform)
        else:
            self.polyline(self.EllipsePoints)

        self.EllipsePoints.clear()
        self.EllipseEngineState = [False, False]

        pass

    # 画无边框的填充椭圆(椭圆外切矩形,旋转角度,旋转基点,绘图计算精度);
    # draw an Solid-ellipse;
    def solidellipse(self, left, top, right, bottom, angle=0, xbase=None, ybase=None, steps=6):
        pencolor(fillcolor())
        width(0)
        begin_fill()

        self.ellipse(left, top, right, bottom, angle, xbase, ybase, steps)

        end_fill()
        pass

    # 画有边框的填充椭圆(椭圆外切矩形,旋转角度,旋转基点,绘图计算精度);
    # Draw a filled ellipse with a border;
    def fillellipse(self, left, top, right, bottom, angle=0, xbase=None, ybase=None, steps=6):
        begin_fill()

        self.ellipse(left, top, right, bottom, angle, xbase, ybase, steps)

        end_fill()
        pass

    def recgradientfill(self, REC, RGB):
        pass


'''------------------------------------------------------------------------------------------
Python根本不适合用来写GUI和渲染引擎,特别是在图形渲染这一块,C++一秒就能完成的计算,Python需要一分钟以上.
而且两者底层代码的复杂程度是差不多的,也就是说在底层这块使用Python并不能很好就降低开发难度. 何况C/C++的
速度对Python来说是降维打击. C/C++能够直接操作内存等计算机资源,当开发者的水平足够高时就能够写出运行速度
非常块并且占用资源非常低的程序.

目前情况是, 本项目: MountPenglai 的运行速度非常的"优雅"(优雅到窒息), 当然主要原因是 turtle 库太慢.
我在C++那边一直在开发的一个项目: Organ-Field GUI 它在做与 MountPenglai 相同图形渲染时目测几毫秒内
就能完成, 而 MountPenglai 则需要破天荒的花上几十秒!
------------------------------------------------------------------------------------------'''

MP = MountPenglai()
MP.initialize(600, 600)
MP.line(0, 300, 600, 300)
MP.line(300, 0, 300, 600)
MP.rectangle(0, 0, 600, 600)

# MP.polyline([300, 300, 200, 200, 100, 200])
# MP.rectangle(100, 100, 200, 200, j, 300, 300)
# MP.polygon(300, 300, 100, 6, 0, 300, 300)
# MP.fillrectangle(200, 200, 300, 300)
# MP.fillellipse(10, 10, 590, 400, 45)

done()
