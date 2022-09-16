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

from MountPenglai import *


# 我几乎没进行过重构和结构优化所以代码写的很烂,可读性也很差;
class MPExamples:
    SelfMP = MountPenglai()
    SelfMPCS = MPColorSystem()
    SelfMath = MountPenglaiMath()

    # 渲染伪3D平面;
    def MPE01(self, Resolution=400):
        clear()
        self.SelfMP.initgraph(Resolution, Resolution)
        self.SelfMP.drawtext(Resolution * 0.5, Resolution * 0.5 + 12, "正在渲染", "微软雅黑", 24, "normal", "center")

        self.SelfMP.BeginBatchDraw()

        for i in range(0, Resolution):
            for j in range(0, Resolution):
                s = 3.0 / (j + 99)
                HD = (int((i + Resolution) * s + j * s) %
                      2 + int((Resolution * 2 - i) * s + j * s) % 2) * 127

                fillcolor(self.SelfMPCS.RGB(HD, HD, HD))
                self.SelfMP.putpixel(i, j)

            if i % 16 == 0:
                self.SelfMP.FlushBatchDraw()

        self.SelfMP.EndBatchDraw()
        pass

    # CircleLineLink;
    def MPE02(self, k_END=0, steps=3, Resolution=900):
        clear()
        self.SelfMP.initgraph(Resolution, Resolution)
        for k in range(k_END):
            self.SelfMP.BeginBatchDraw()
            clear()

            origin = [Resolution * 0.5, Resolution * 0.5]
            CirclePoints = []

            for i in range(0, 360, steps):
                x, y = self.SelfMP.RotationMatrix(
                    1.9 * origin[0], origin[1], origin[0], origin[1], i)
                self.SelfMP.putpixel(x, y, 6)

                CirclePoints.append(int(x))
                CirclePoints.append(int(y))

            pensize(1)

            i = 0
            j = 0
            H = 0
            while True:
                m = k * i % int(360 / steps)
                pencolor(self.SelfMPCS.HSV(H, 0.6, 0.8))
                self.SelfMP.line(
                    CirclePoints[i], CirclePoints[i + 1], CirclePoints[m], CirclePoints[m + 1])
                self.SelfMP.FlushBatchDraw()

                j += 1
                H += steps
                if j == int(len(CirclePoints) / 2) - 1:
                    break
                i += 2

            self.SelfMP.EndBatchDraw()
        pass

    # [分形] 渲染 Mandelbrot Set (曼德布洛特集);
    def MPE03(self, width=400, height=300):
        clear()
        self.SelfMP.initgraph(width, height)
        self.SelfMP.drawtext(width * 0.5, height * 0.5 +
                             12, "正在渲染", "微软雅黑", 24, "normal", "center")

        self.SelfMP.BeginBatchDraw()

        c_re = 0
        c_im = 0
        z_re = 0
        z_im = 0
        for x in range(0, width):
            c_re = -2.1 + (1.1 - (-2.1)) * (x / width)
            for y in range(0, height):
                c_im = -1.2 + (1.2 - -1.2) * (y / height)
                z_re = z_im = 0

                H = 0
                for k in range(0, 180):
                    H = k
                    if z_re * z_re + z_im * z_im > 4.0:
                        break

                    z_re, z_im = self.SelfMath.COMPLEXSUM(
                        self.SelfMath.COMPLEXMUL((z_re, z_im), (z_re, z_im)), (c_re, c_im))

                fillcolor(self.SelfMPCS.HSV(
                    float(((H << 5) % 360)) + 60, 1, 1))
                self.SelfMP.putpixel(x, y)

            if x % 16 == 0:
                self.SelfMP.FlushBatchDraw()

        self.SelfMP.EndBatchDraw()
        pass

    # Organ-Field GUI 风格时钟(我把我一年半前的祖传C++代码移植过来了);
    def MPE04(self, Resolution=900):
        clear()
        from datetime import datetime
        halfResolution = 0.5 * Resolution
        Resolution0_1 = 0.1 * Resolution
        Resolution0_3 = 0.3 * Resolution
        R = Resolution0_4 = 0.4 * Resolution
        Resolution0_45 = 0.45 * Resolution
        halfResolution0_01 = 0.01 * halfResolution
        halfResolution0_021 = 0.021 * halfResolution
        halfResolution0_035 = 0.035 * halfResolution
        halfResolution0_04 = 0.04 * halfResolution
        wochentag = ["MONDAY", "TUESDAY", "WEDNESDAY",
                     "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

        SX0 = []
        SY0 = []
        SXS = []
        SYS = []
        Second = 0
        while Second < 2 * pi:
            Second = (2 * pi / 60) + Second

            SXS.append(int((R - 20) * cos(Second)))
            SX0.append(int((R - 40) * cos(Second)))

            SYS.append(int((R - 20) * sin(Second)))
            SY0.append(int((R - 40) * sin(Second)))

        BX0 = []
        BY0 = []
        BXS = []
        BYS = []
        Second = 0
        while Second < 2 * pi:
            Second = (2 * pi / 12) + Second

            BXS.append(int((R - 20) * cos(Second)))
            BX0.append(int((R - 52) * cos(Second)))

            BYS.append(int((R - 20) * sin(Second)))
            BY0.append(int((R - 52) * sin(Second)))

        XT = []
        YT = []
        Second = 0
        while Second < 2 * pi:
            Second = (2 * pi / 12) + Second

            XT.append(int((R - 90) * cos(Second)))
            YT.append(int((R - 90) * sin(Second)))

        Angle_Precompute = (2 * pi) / 60
        Angle_H_Precompute = (2 * pi) / 12

        AC = 180 / pi

        self.SelfMP.BeginBatchDraw()
        self.SelfMP.initgraph(Resolution, Resolution)
        setundobuffer(63)
        while True:
            self.SelfMP.radialgradient(
                halfResolution, halfResolution, Resolution0_4, Resolution0_45, "#23272e", "#282c34", 2)

            fillcolor("#313640")
            self.SelfMP.solidcircle(
                halfResolution, halfResolution, Resolution0_4)

            self.SelfMP.radialgradient(
                halfResolution, halfResolution, Resolution0_3, Resolution0_1, "#313640", "#282c34", 2)
            fillcolor("#282c34")
            self.SelfMP.solidcircle(
                halfResolution, halfResolution, Resolution0_1)

            pensize(4)
            pencolor("#737780")
            for i in range(60):
                self.SelfMP.line(SX0[i] + halfResolution, SY0[i] + halfResolution,
                                 SXS[i] + halfResolution, SYS[i] + halfResolution)

            pensize(8)
            pencolor("#737780")
            for i in range(12):
                self.SelfMP.line(BX0[i] + halfResolution, BY0[i] + halfResolution,
                                 BXS[i] + halfResolution, BYS[i] + halfResolution)

            pencolor("#abb2bf")
            TextNum = 4
            for i in range(12):
                if TextNum > 12:
                    TextNum = 1
                self.SelfMP.drawtext(XT[i] + halfResolution, YT[i] + halfResolution + 21, str(
                    int(TextNum)), "微软雅黑", 24, "normal", "center")
                TextNum += 1

            pencolor("#676b73")
            self.SelfMP.drawtext(halfResolution, halfResolution -
                                 0.3 * R, "R M S H E", "微软雅黑", 24, "normal", "center")

            t1 = datetime.today()
            self.SelfMP.drawtext(halfResolution, halfResolution + 26 + 0.3 * R,
                                 wochentag[t1.weekday()], "微软雅黑", 24, "normal", "center")

            MinuteNLast = MinuteNow = t1.minute
            while True:
                # // 计算时、分、秒针的弧度值;
                t = datetime.today()
                # Angle_MicroSecond = t.microsecond * (2 * pi) / 60
                # Angle_Second = t.second * (2 * pi) / 60 + Angle_MicroSecond * 0.000001

                MinuteNow = t.minute
                if MinuteNow - MinuteNLast == 2:
                    clear()
                    break

                Angle_Second = t.second * Angle_Precompute
                Angle_Minute = t.minute * Angle_Precompute + Angle_Second / 60
                Angle_Hour = t.hour * Angle_H_Precompute + Angle_Minute / 12

                # // 计算时、分、秒针的坐标;
                Angle_Second_cos = cos(Angle_Second)
                Angle_Second_sin = sin(Angle_Second)
                Second_Y = -(R - 62) * Angle_Second_cos + halfResolution
                Y0 = -(-R + 320) * Angle_Second_cos + halfResolution
                Second_X = (R - 62) * Angle_Second_sin + halfResolution
                X0 = (-R + 320) * Angle_Second_sin + halfResolution

                Minute_hand_Y = -(R - 90) * cos(Angle_Minute) + halfResolution
                Minute_hand_X = (R - 90) * sin(Angle_Minute) + halfResolution

                Hour_hand_Y = -(R - 120) * cos(Angle_Hour) + halfResolution
                Hour_hand_X = (R - 120) * sin(Angle_Hour) + halfResolution

                # //指针圆心投影;
                fillcolor("#23272e")
                self.SelfMP.solidcircle(
                    halfResolution + 3, halfResolution + 3, halfResolution0_04)

                # //分针投影;
                pencolor("#282c34")
                pensize(12)
                self.SelfMP.line(halfResolution + 5, halfResolution +
                                 5, Minute_hand_X + 5, Minute_hand_Y + 5)

                # //时针投影;
                pencolor("#23272e")
                pensize(14)
                self.SelfMP.line(halfResolution + 5, halfResolution +
                                 5, Hour_hand_X + 5, Hour_hand_Y + 5)

                # // 时针;
                pensize(12)
                pencolor("#959ba6")
                self.SelfMP.line(halfResolution, halfResolution,
                                 Hour_hand_X, Hour_hand_Y)

                # // 分针;
                pensize(8)
                pencolor("#abb2bf")
                self.SelfMP.line(halfResolution, halfResolution,
                                 Minute_hand_X, Minute_hand_Y)

                # // 分针圆心;
                fillcolor("#abb2bf")
                self.SelfMP.solidcircle(
                    halfResolution, halfResolution, halfResolution0_035)

                # // 秒针;
                ASAC = Angle_Second * AC
                pensize(4)
                pencolor(self.SelfMPCS.HSV(ASAC, 0.5, 0.8))
                self.SelfMP.line(X0, Y0, Second_X, Second_Y)

                # // 秒针圆心;
                fillcolor(self.SelfMPCS.HSV(ASAC, 0.5, 0.8))
                self.SelfMP.solidcircle(
                    halfResolution, halfResolution, halfResolution0_021)

                # // 圆心;
                fillcolor("#313640")
                self.SelfMP.solidcircle(
                    halfResolution, halfResolution, halfResolution0_01)

                self.SelfMP.FlushBatchDraw()
                # self.SelfMP.saveimage("01")

                # 刷新视图;
                for i in range(64):
                    undo()

    def Tips(self):
        self.SelfMP.initgraph(1280, 720, "#a4262c")
        pencolor("#ecf0f1")
        self.SelfMP.drawtext(640, 360 + 15, "程序执行需要一定时间(大约2分钟左右)请耐心等待", "微软雅黑", 36, "normal", "center")
        self.SelfMP.drawtext(640, 360 + 50, "Powered by RMSHE in [303132303430323139]", "微软雅黑", 16, "normal", "center")
        time.sleep(5)
        pass


# 程序执行需要一定时间(大约2分钟才能执行完毕),请耐心等待;
MPE = MPExamples()
MPE.Tips()
MPE.MPE02(14, 1)  # 取圆上 int(360 / steps) 个均布点,对于k计算每一个n对应kn除以 int(360 / steps) 的余数m,连接n与m;
MPE.MPE01(200)  # 渲染伪3D平面(演示分辨率我已经调的很低了,参数千万不要乱改,不然渲染会非常卡,非常慢);
MPE.MPE03(150, 100)  # 渲染Mandelbrot Set分形(演示分辨率我已经调的很低了,参数千万不要乱改,不然渲染会非常卡,非常慢);
MPE.MPE04()  # Organ-Field GUI 风格时钟(我把我一年半前的祖传C++代码移植过来了);
