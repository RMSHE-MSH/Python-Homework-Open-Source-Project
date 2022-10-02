from ctypes import *
from math import *
import os

os.chdir('F:\\Subject\\Python\\Python-Homework-Open-Source-Project\\EasyX Graphics Library for Python\\x64\\Release\\')
pDll = CDLL("./EasyX Graphics Library for Python.dll")

# 调用动态链接库函数
pDll.c_initgraph(900, 900)

k = 0
for i in range(900):
    for j in range(900):
        pDll.c_putpixel(i, j, pDll.c_HSVtoRGB(
            c_float(360*abs(sin(k))), c_float(0.7), c_float(1)))

    k += 0.001

os.system("pause")
