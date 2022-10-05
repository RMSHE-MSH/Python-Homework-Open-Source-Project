from math import pi
from time import sleep
from ctypes import *
import os

os.chdir('F:\\Subject\\Python\\Python-Homework-Open-Source-Project\\EasyX Graphics Library for Python\\x64\\Release\\')
pDll = CDLL("./EasyX Graphics Library for Python.dll")

TRANSPARENT = 1
OPAQUE = 2

BS_SOLID = 0
BS_NULL = 1
BS_HATCHED = 2
BS_PATTERN = 3
BS_DIBPATTERN = 5

HS_HORIZONTAL = 0
HS_VERTICAL = 1
HS_FDIAGONAL = 2
HS_BDIAGONAL = 3
HS_CROSS = 4
HS_DIAGCROSS = 5

PS_SOLID = 0
PS_DASH = 1
PS_DOT = 2
PS_DASHDOT = 3
PS_DASHDOTDOT = 4
PS_NULL = 5

PS_ENDCAP_ROUND = 0x00000000
PS_ENDCAP_SQUARE = 0x00000100
PS_ENDCAP_FLAT = 0x00000200


# VectorStack(图形矢量堆栈)相关函数;


def pop():
    pDll.c_pop_vecstack()


def back():
    pDll.c_back_vecstack()


# 绘图设备相关函数;


def cleardevice():
    pDll.c_cleardevice()


def initgraph(x=600, y=600, color=3419176):  # RGB(40, 44, 52);
    return pDll.c_initgraph(c_int(x), c_int(y), c_ulong(color))


def closegraph():
    pDll.c_closegraph()


def setaspectratio(x=1.0, y=1.0):
    pDll.c_setaspectratio(c_float(x), c_float(y))


def graphdefaults():
    pDll.c_graphdefaults()


def setorigin(x=0, y=0):
    pDll.c_setorigin(c_int(x), c_int(y))


# 颜色模型;


def GetBValue(rgb):
    return pDll.c_GetBValue(c_ulong(rgb))


def GetGValue(rgb):
    return pDll.c_GetGValue(c_ulong(rgb))


def GetRValue(rgb):
    return pDll.c_GetRValue(c_ulong(rgb))


def HSLtoRGB(H, S, L):
    return pDll.c_HSLtoRGB(c_float(H), c_float(S), c_float(L))


def HSVtoRGB(H, S, V):
    return pDll.c_HSVtoRGB(c_float(H), c_float(S), c_float(V))


def RGB(byRed, byGreen, byBlue):
    return pDll.c_RGB(c_byte(byRed), c_byte(byGreen), c_byte(byBlue))


def RGBtoGRAY(rgb):
    return pDll.c_RGBtoGRAY(c_ulong(rgb))


# 图形颜色及样式设置相关函数;


def getbkcolor():
    return pDll.c_getbkcolor()


def getbkmode():
    return pDll.c_getbkmode()


def getfillcolor():
    return pDll.c_getfillcolor()


def getlinecolor():
    return pDll.c_getlinecolor()


def setbkcolor(color=3419176):  # RGB(40, 44, 52);
    pDll.c_setbkcolor(c_ulong(color))


def setbkmode(mode=TRANSPARENT):
    pDll.c_setbkmode(c_int(mode))


def setfillcolor(color=15724527):  # RGB(239,239,239);
    pDll.c_setfillcolor(c_ulong(color))


def setfillstyle(style=BS_SOLID, hatch=None):
    pDll.c_setfillstyle(c_int(style), c_long(hatch))


def setlinecolor(color=15724527):  # RGB(239,239,239);
    pDll.c_setlinecolor(c_ulong(color))


def setlinestyle(thickness=1, style=PS_SOLID | PS_ENDCAP_ROUND):
    pDll.c_setlinestyle(c_int(style), c_int(thickness))


# 图形绘制相关函数;


def arc(left, top, right, bottom, stangle, endangle):
    pDll.c_arc(c_int(left), c_int(top), c_int(right), c_int(bottom), c_double(stangle), c_double(endangle))


def circle(x, y, radius):
    pDll.c_circle(c_int(x), c_int(y), c_int(radius))


def clearcircle(x, y, radius):
    pDll.c_clearcircle(c_int(x), c_int(y), c_int(radius))


def clearellipse(left, top, right, bottom):
    pDll.c_clearellipse(c_int(left), c_int(top), c_int(right), c_int(bottom))


def clearpie(left, top, right, bottom, stangle=0, endangle=2*pi):
    pDll.c_clearpie(c_int(left), c_int(top), c_int(right), c_int(bottom), c_double(stangle), c_double(endangle))


def clearpolygon(points=()):
    pDll.c_clearpolygon((c_int*len(points))(*points), len(points))


def clearrectangle(left, top, right, bottom):
    pDll.c_clearrectangle(c_int(left), c_int(top), c_int(right), c_int(bottom))


def clearroundrect(left, top, right, bottom, ellipsewidth, ellipseheight):
    pDll.c_clearroundrect(c_int(left), c_int(top), c_int(right), c_int(bottom), c_int(ellipsewidth), c_int(ellipseheight))


def ellipse(left, top, right, bottom):
    pDll.c_ellipse(c_int(left), c_int(top), c_int(right), c_int(bottom))


def fillcircle(x, y, radius):
    pDll.c_fillcircle(c_int(x), c_int(y), c_int(radius))


def fillellipse(left, top, right, bottom):
    pDll.c_fillellipse(c_int(left), c_int(top), c_int(right), c_int(bottom))


def fillpie(left, top, right, bottom,  stangle=0, endangle=2*pi):
    pDll.c_fillpie(c_int(left), c_int(top), c_int(right), c_int(bottom), c_double(stangle), c_double(endangle))


def putpixel(x, y):
    pDll.c_putpixel(c_int(x), c_int(y))

# 其它函数;


def BeginBatchDraw():
    pDll.c_BeginBatchDraw()


def EndBatchDraw():
    pDll.c_EndBatchDraw()


def FlushBatchDraw():
    pDll.c_FlushBatchDraw()


initgraph()
setlinestyle(1)

BeginBatchDraw()
for i in range(0,600,8):
    for j in range(0, 600, 8):
        putpixel(j, i)

FlushBatchDraw()
sleep(1)

for i in range(0, 600, 8):
    for j in range(0, 600, 8):
        back()
        FlushBatchDraw()

EndBatchDraw()


os.system("pause")
