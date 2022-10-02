from ctypes import *
import os

pDll = CDLL("./EasyX Graphics Library for Python.dll")

#调用动态链接库函数
pDll.c_initgraph(800, 800)
pDll.c_circle(400,400,300)

os.system("pause")