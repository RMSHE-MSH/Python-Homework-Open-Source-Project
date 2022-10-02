//Powered by RMSHE / 2022.10.02;
#pragma once
#include "Universal.h"

#define EASYX_API extern "C" __declspec(dllexport)

//绘图设备相关函数;
EASYX_API void c_cleardevice();

EASYX_API HWND c_initgraph(int width, int height, int flag = EW_SHOWCONSOLE);

EASYX_API void c_closegraph();

EASYX_API void c_setaspectratio(float x, float y);

EASYX_API void c_graphdefaults();

EASYX_API void c_setorigin(int x, int y);

//颜色模型;
EASYX_API BYTE c_GetBValue(COLORREF rgb);

EASYX_API BYTE c_GetGValue(COLORREF rgb);

EASYX_API BYTE c_GetRValue(COLORREF rgb);

EASYX_API COLORREF c_HSLtoRGB(float H, float S, float L);

EASYX_API COLORREF c_HSVtoRGB(float H, float S, float V);

EASYX_API COLORREF c_RGB(BYTE byRed, BYTE byGreen, BYTE byBlue);

EASYX_API void c_putpixel(int x, int y, COLORREF color);

EASYX_API void c_circle(int x, int y, int radius);
