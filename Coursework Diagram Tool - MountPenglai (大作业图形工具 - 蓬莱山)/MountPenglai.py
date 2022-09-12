'''-----------------------------------------------------------------------------
Powered by RMSHE / 2022.09.08;

将 turtle 的绘图逻辑更改为 Organ-Field GUI 样式;
Organ-Field GUI 的绘图逻辑我参考的是 AutoCAD;
turtle 的使用逻辑过于直观,因此造成了使用不便,翻了一遍文档,
还好基础该有的都有,我要重新将它封装成C++图形库的使用逻辑;

项目代号: 蓬莱山(MountPenglai) / 生命周期: 一个月(大作业结束可能就不值得我继续维护了);
还有,开发时间不足代码是赶出来的屎山能跑就行;
-----------------------------------------------------------------------------'''
from turtle import *
from math import *
import _thread


# 色彩变换是图像处理中最重要的一环
# (这部分我引入一些仿 Photoshop Camera Raw 色彩处理功能,当然PS是C++写的我也不知道它的代码,我只是根据公开的公式对部分功能进行仿制);
class MPColorSystem:
    # RGB to HEX; More details on RGB: https://en.wikipedia.org/wiki/RGB_color_model
    def RGB(self, R, G, B):
        return str("#" + ('{:02X}' * 3).format(R, G, B))

    # HSV to HEX; More details on HSV: https://en.wikipedia.org/wiki/HSL_and_HSV
    def HSV(self, H, S, V):
        R, G, B = self.HSVtoRGB(H, S, V)
        return self.RGB(R, G, B)

    # HEX to RGB;
    def GetRGBValue(self, ColorHex):
        return tuple(int(ColorHex[1:][i:i + 2], 16) for i in (0, 2, 4))

    # 返回指定HEX颜色值中的红色分量;
    # Returns the red decomposition of the HEX color value;
    def GetRValue(self, ColorHex):
        return self.GetRGBValue(ColorHex)[0]

    # 返回指定HEX颜色值中的绿色分量;
    # Returns the green decomposition of the HEX color value;
    def GetGValue(self, ColorHex):
        return self.GetRGBValue(ColorHex)[1]

    # 返回指定HEX颜色值中的蓝色分量;
    # Returns the blue decomposition of the HEX color value;
    def GetBValue(self, ColorHex):
        return self.GetRGBValue(ColorHex)[2]

    # HEX to HSV;
    def GetHSVValue(self, ColorHex):
        R, G, B = self.GetRGBValue(ColorHex)
        return self.RGBtoHSV(R, G, B)

    # 返回指定HEX颜色值中的色相分量;
    # Returns the Hue decomposition of the HEX color value;
    def GetHValue(self, ColorHex):
        return self.GetHSVValue(ColorHex)[0]

    # 返回指定HEX颜色值中的饱和度分量;
    # Returns the Saturation decomposition of the HEX color value;
    def GetSValue(self, ColorHex):
        return self.GetHSVValue(ColorHex)[1]

    # 返回指定HEX颜色值中的明度分量;
    # Returns the Value decomposition of the HEX color value;
    def GetVValue(self, ColorHex):
        return self.GetHSVValue(ColorHex)[2]

    # HSV色彩空间转RGB色彩空间(色相分量,饱和度分量,明度分量);
    # HSV to RGB(Hue,Saturation,Value);
    def HSVtoRGB(self, H, S, V):
        if not (0.0 <= H <= 360.0 and 0.0 <= S <= 1.0 and 0.0 <= V <= 1.0):
            return "Parameter error."

        C = V * S
        X = C * (1 - abs((H / 60) % 2 - 1))
        m = V - C

        RGB2 = []
        if 0.0 <= H <= 60.0:
            RGB2 = [C, X, 0]
        elif 60.0 <= H <= 120.0:
            RGB2 = [X, C, 0]
        elif 120.0 <= H <= 180.0:
            RGB2 = [0, C, X]
        elif 180.0 <= H <= 240.0:
            RGB2 = [0, X, C]
        elif 240.0 <= H <= 300.0:
            RGB2 = [X, 0, C]
        elif 300.0 <= H <= 360.0:
            RGB2 = [C, 0, X]

        return int((RGB2[0] + m) * 255), int((RGB2[1] + m) * 255), int((RGB2[2] + m) * 255)

    # RGB色彩空间转HSV色彩空间(R,G,B);
    # RGB to HSV;
    def RGBtoHSV(self, R, G, B):
        r_, g_, b_ = R / 255, G / 255, B / 255
        c_max = max(r_, g_, b_)
        c_min = min(r_, g_, b_)
        dela = c_max - c_min

        h = None
        if dela == 0:
            h = 0
        elif c_max == r_:
            h = 60 * (((g_ - b_) / dela) % 6)
        elif c_max == g_:
            h = 60 * ((b_ - r_) / dela + 2)
        elif c_max == b_:
            h = 60 * ((r_ - g_) / dela + 4)

        s = 0 if c_max == 0 else dela / c_max
        v = c_max

        return h, s, v

    # 返回与指定RGB颜色对应的灰度值颜色;
    # RGB to GrayScale(R,G,B)
    def RGBtoGRAY(self, R, G, B):
        return (R * 38 + G * 75 + B * 15) >> 7

    # RGB色彩通道提取:提取像素组的特定颜色通道,并且支持自定义提取范围(像素组颜色的十六进制值列表,提取通道[R,G,B],提取范围[0,255],其余通道填充值);
    # RGB color channel extraction: extracts specific color channels of pixel groups, and supports custom extraction range;
    def RGBChannelExtraction(self, ColorGroupHex=(), Channel="R", MIN=0, MAX=255, Fill=(0, 0, 0)):
        ChannelValue = {"R": Fill[0], "G": Fill[1], "B": Fill[2]}
        OutputChannelGroupHex = []
        for i in ColorGroupHex:
            if Channel == "R":
                ChannelValue["R"] = self.GetRValue(i)
                if not MIN <= ChannelValue["R"] <= MAX:
                    ChannelValue["R"] = Fill[0]

            elif Channel == "G":
                ChannelValue["G"] = self.GetGValue(i)
                if not MIN <= ChannelValue["G"] <= MAX:
                    ChannelValue["G"] = Fill[1]

            elif Channel == "B":
                ChannelValue["B"] = self.GetBValue(i)
                if not MIN <= ChannelValue["B"] <= MAX:
                    ChannelValue["B"] = Fill[2]

            OutputChannelGroupHex.append(self.RGB(ChannelValue["R"], ChannelValue["G"], ChannelValue["B"]))

        return OutputChannelGroupHex

    # RGB色彩通道编辑:提取像素组特点通道后将其值替换为指定值,并且支持自定义编辑范围(像素组颜色的十六进制值列表,需要编辑的通道[R,G,B],替换值[0,255],编辑范围[0,255]);
    # RGB color channel edit: After extracts the pixel group specific channel, replace its value with the specified value, and support custom edit range.
    def RGBChannelEdit(self, ColorGroupHex=(), Channel="R", AlternateValue=None, MIN=0, MAX=255):
        ChannelValue = {"R": 0, "G": 0, "B": 0}
        OutputChannelGroupHex = []
        for i in ColorGroupHex:
            if Channel == "R":
                R, G, B = self.GetRGBValue(i)
                if MIN <= R <= MAX:
                    ChannelValue["R"] = AlternateValue
                else:
                    ChannelValue["R"] = R

                ChannelValue["G"] = G
                ChannelValue["B"] = B

            elif Channel == "G":
                R, G, B = self.GetRGBValue(i)
                if MIN <= G <= MAX:
                    ChannelValue["G"] = AlternateValue
                else:
                    ChannelValue["G"] = G

                ChannelValue["R"] = R
                ChannelValue["B"] = B


            elif Channel == "B":
                R, G, B = self.GetRGBValue(i)
                if MIN <= B <= MAX:
                    ChannelValue["B"] = AlternateValue
                else:
                    ChannelValue["B"] = B

                ChannelValue["R"] = R
                ChannelValue["G"] = G

            OutputChannelGroupHex.append(self.RGB(ChannelValue["R"], ChannelValue["G"], ChannelValue["B"]))

        return OutputChannelGroupHex

    # RGB色彩通道线性偏移:提取像素组特点通道后将其值偏移,并且支持自定义编辑范围(像素组颜色的十六进制值列表,需要编辑的通道[R,G,B],偏移量,编辑范围[0,255]);
    # RGB color channel linear drift: extract the pixel group specific channel and drift its value;
    def RGBChannelDrift(self, ColorGroupHex=(), Channel="R", DriftValue=None, MIN=0, MAX=255):
        ChannelValue = {"R": 0, "G": 0, "B": 0}
        OutputChannelGroupHex = []
        for i in ColorGroupHex:
            if Channel == "R":
                R, G, B = self.GetRGBValue(i)
                if MIN <= R <= MAX:
                    composite = R + DriftValue
                    if composite > 255:
                        composite = 255
                    elif composite < 0:
                        composite = 0

                    ChannelValue["R"] = composite
                else:
                    ChannelValue["R"] = R

                ChannelValue["G"] = G
                ChannelValue["B"] = B

            elif Channel == "G":
                R, G, B = self.GetRGBValue(i)
                if MIN <= G <= MAX:
                    composite = G + DriftValue
                    if composite > 255:
                        composite = 255
                    elif composite < 0:
                        composite = 0

                    ChannelValue["G"] = composite
                else:
                    ChannelValue["G"] = G

                ChannelValue["R"] = R
                ChannelValue["B"] = B


            elif Channel == "B":
                R, G, B = self.GetRGBValue(i)
                if MIN <= B <= MAX:
                    composite = B + DriftValue
                    if composite > 255:
                        composite = 255
                    elif composite < 0:
                        composite = 0

                    ChannelValue["B"] = composite
                else:
                    ChannelValue["B"] = B

                ChannelValue["R"] = R
                ChannelValue["G"] = G

            OutputChannelGroupHex.append(self.RGB(ChannelValue["R"], ChannelValue["G"], ChannelValue["B"]))

        return OutputChannelGroupHex

    # HSV色彩通道提取:提取像素组的特定颜色通道,并且支持自定义提取范围(像素组颜色的十六进制值列表,提取通道[H,S,V],提取范围{H:[0,360],S:[0,1],V:[0,1]},其余通道填充值);
    # HSV color channel linear drift: extract the pixel group specific channel and drift its value;
    def HSVChannelExtraction(self, ColorGroupHex=(), Channel="H", MIN=0.0, MAX=360.0, Fill=(0.0, 1.0, 1.0)):
        if Channel != "H" and MAX > 1.0:
            MAX = 1

        OutputChannelGroupHex = []
        for i in ColorGroupHex:
            ChannelValue = {"H": Fill[0], "S": Fill[1], "V": Fill[2]}
            if Channel == "H":
                ChannelValue["H"] = self.GetHValue(i)
                if not MIN <= ChannelValue["H"] <= MAX:
                    ChannelValue["H"] = Fill[0]
                    ChannelValue["S"] = 0.0
                    ChannelValue["V"] = 0.0

            elif Channel == "S":
                ChannelValue["S"] = self.GetSValue(i)
                if not MIN <= ChannelValue["S"] <= MAX:
                    ChannelValue["S"] = Fill[1]
                    ChannelValue["V"] = 0.0

            elif Channel == "V":
                ChannelValue["V"] = self.GetVValue(i)
                if not MIN <= ChannelValue["V"] <= MAX:
                    ChannelValue["S"] = 0.0
                    ChannelValue["V"] = Fill[2]

            OutputChannelGroupHex.append(self.HSV(ChannelValue["H"], ChannelValue["S"], ChannelValue["V"]))

        return OutputChannelGroupHex

    # HSV色彩通道编辑(值替换);
    # 将像素组的HSV颜色通道全部提取出来,然后选择一个通道作为基通道,并且选择基通道的范围,最后选择要编辑的通道并指定替换值.程序将会把基通道范围内的编辑通道值替换为指定值;
    # 例如: 我对鲜花拍摄了一张照片,这张照片的蓝色部分饱和度太高,那么我们编辑的通道就是饱和度通道(EditChannel = "S"),替换值我们将其设为较低的值(AlternateValue = 0.3),
    # 我们指定基通道为色相通道(BaseChannel = "H"),基通道范围为图片都蓝色部分(大致在MIN = 180°到MAX = 300°之间).这样程序就会将基通道的蓝色颜色的饱和度整体替换为一个低值.
    # 这一过程中我们只改变了图片中蓝色颜色像素的饱和度,其他颜色不受影响,而且蓝色颜色的色相和明度也不受影响.
    # HSVChannelEdit(像素组颜色的十六进制值列表,编辑通道[H/S/V],替换值,基通道[H/S/V],基通道范围);
    # 注意:当编辑通道为H时,替换值必须在[0,360]区间内; 当编辑通道为S或V时,替换值必须在[0,1]区间内;
    # 当基通道为H时,基通道范围MIN-MAX必须在[0,360]区间内; 当基通道为S或V时基通道范围MIN-MAX必须在[0,1]区间内;
    def HSVChannelEdit(self, ColorGroupHex=(), EditChannel="H", AlternateValue=0.0, BaseChannel="H", MIN=0.0, MAX=360.0):
        BC = {"H": 0, "S": 1, "V": 2}

        if EditChannel != "H":
            if AlternateValue < 0.0:
                AlternateValue = abs(AlternateValue)
            if AlternateValue > 1.0:
                AlternateValue = 1.0
        else:
            if AlternateValue < 0.0:
                AlternateValue = abs(AlternateValue)
            if AlternateValue > 360.0:
                AlternateValue = 360.0

        if BaseChannel != "H":
            if MIN < 0.0:
                MIN = abs(MIN)
            if MIN > 1.0:
                MIN = 0.0

            if MAX < 0.0:
                MAX = abs(MAX)
            if MAX > 1.0:
                MAX = 1.0
        else:
            if MIN < 0.0:
                MIN = abs(MIN)
            if MIN > 360.0:
                MIN = 0.0
            if MAX < 0.0:
                MAX = abs(MAX)
            if MAX > 360.0:
                MAX = 360.0

        global ChannelValue
        OutputChannelGroupHex = []
        for i in ColorGroupHex:
            ChannelValue = {"H": 0.0, "S": 1.0, "V": 1.0}
            if EditChannel == "H":
                HSV = self.GetHSVValue(i)

                if MIN <= HSV[BC[BaseChannel]] <= MAX:
                    ChannelValue["H"] = AlternateValue
                else:
                    ChannelValue["H"] = HSV[0]

                ChannelValue["S"] = HSV[1]
                ChannelValue["V"] = HSV[2]

            elif EditChannel == "S":
                HSV = self.GetHSVValue(i)
                if MIN <= HSV[BC[BaseChannel]] <= MAX:
                    ChannelValue["S"] = AlternateValue
                else:
                    ChannelValue["S"] = HSV[1]

                ChannelValue["H"] = HSV[0]
                ChannelValue["V"] = HSV[2]

            elif EditChannel == "V":
                HSV = self.GetHSVValue(i)
                if MIN <= HSV[BC[BaseChannel]] <= MAX:
                    ChannelValue["V"] = AlternateValue
                else:
                    ChannelValue["V"] = HSV[2]

                ChannelValue["H"] = HSV[0]
                ChannelValue["S"] = HSV[1]

            OutputChannelGroupHex.append(self.HSV(ChannelValue["H"], ChannelValue["S"], ChannelValue["V"]))

        return OutputChannelGroupHex

    # HSV色彩通道偏移(值偏移);
    # 将像素组的HSV颜色通道全部提取出来,然后选择一个通道作为基通道,并且选择基通道的范围,最后选择要编辑的通道并指定偏移量.程序将会把基通道范围内的编辑通道值偏移;
    # 例如: 我对鲜花拍摄了一张照片,这张照片的蓝色部分饱和度太高,那么我们编辑的通道就是饱和度通道(EditChannel = "S"),偏移量我们将其设为负值(DriftValue = -0.5),
    # 我们指定基通道为色相通道(BaseChannel = "H"),基通道范围为图片都蓝色部分(大致在MIN = 180°到MAX = 300°之间).这样程序就会将基通道的蓝色颜色的饱和度整体向下偏移.
    # 这一过程中我们只改变了图片中蓝色颜色像素的饱和度,其他颜色不受影响,而且蓝色颜色的色相和明度也不受影响.
    # HSVChannelEdit(像素组颜色的十六进制值列表,编辑通道[H/S/V],偏移量,基通道[H/S/V],基通道范围);
    # 注意:当编辑通道为H时,偏移量尽量在[-360,360]区间内; 当编辑通道为S或V时,偏移量尽量在[-1,1]区间内;
    # 当基通道为H时,基通道范围MIN-MAX必须在[0,360]区间内; 当基通道为S或V时基通道范围MIN-MAX必须在[0,1]区间内;
    def HSVChannelDrift(self, ColorGroupHex=(), EditChannel="H", DriftValue=0.0, BaseChannel="H", MIN=0.0, MAX=360.0):
        BC = {"H": 0, "S": 1, "V": 2}

        if BaseChannel != "H":
            if MIN < 0.0:
                MIN = abs(MIN)
            if MIN > 1.0:
                MIN = 0.0

            if MAX < 0.0:
                MAX = abs(MAX)
            if MAX > 1.0:
                MAX = 1.0
        else:
            if MIN < 0.0:
                MIN = abs(MIN)
            if MIN > 360.0:
                MIN = 0.0
            if MAX < 0.0:
                MAX = abs(MAX)
            if MAX > 360.0:
                MAX = 360.0

        global ChannelValue
        OutputChannelGroupHex = []
        for i in ColorGroupHex:
            ChannelValue = {"H": 0.0, "S": 1.0, "V": 1.0}
            if EditChannel == "H":
                HSV = self.GetHSVValue(i)

                if MIN <= HSV[BC[BaseChannel]] <= MAX:
                    ChannelValue["H"] = HSV[0] + DriftValue

                    if ChannelValue["H"] > 360.0:
                        ChannelValue["H"] = ChannelValue["H"] - 360.0
                    elif ChannelValue["H"] < 0:
                        ChannelValue["H"] = abs(ChannelValue["H"])

                else:
                    ChannelValue["H"] = HSV[0]

                ChannelValue["S"] = HSV[1]
                ChannelValue["V"] = HSV[2]

            elif EditChannel == "S":
                HSV = self.GetHSVValue(i)
                if MIN <= HSV[BC[BaseChannel]] <= MAX:
                    ChannelValue["S"] = HSV[1] + DriftValue

                    if ChannelValue["S"] > 1.0:
                        ChannelValue["S"] = 1.0
                    elif ChannelValue["S"] < 0:
                        ChannelValue["S"] = 0

                else:
                    ChannelValue["S"] = HSV[1]

                ChannelValue["H"] = HSV[0]
                ChannelValue["V"] = HSV[2]

            elif EditChannel == "V":
                HSV = self.GetHSVValue(i)
                if MIN <= HSV[BC[BaseChannel]] <= MAX:
                    ChannelValue["V"] = HSV[2] + DriftValue

                    if ChannelValue["V"] > 1.0:
                        ChannelValue["V"] = 1.0
                    elif ChannelValue["V"] < 0:
                        ChannelValue["V"] = 0

                else:
                    ChannelValue["V"] = HSV[2]

                ChannelValue["H"] = HSV[0]
                ChannelValue["S"] = HSV[1]

            OutputChannelGroupHex.append(self.HSV(ChannelValue["H"], ChannelValue["S"], ChannelValue["V"]))

        return OutputChannelGroupHex


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

        pencolor("#abb2bf")
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

    # 将画布导出为矢量图(文件名);
    # Export the canvas as a vector image;
    def saveimage(self, fileName):
        IMG = getscreen()
        IMG.getcanvas().postscript(file=str(fileName) + "_RMSHE_MountPenglai_Vector.eps")
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
