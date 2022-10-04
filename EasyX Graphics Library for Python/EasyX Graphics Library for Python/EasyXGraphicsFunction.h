//Powered by RMSHE / 2022.10.02;
#pragma once
#include "Universal.h"

#define EASYX_API extern "C" __declspec(dllexport)

//VectorStack(图形矢量堆栈)相关函数;

EASYX_API void c_pop_vecstack();

EASYX_API void c_back_vecstack();

//绘图设备相关函数;

EASYX_API void c_cleardevice();

EASYX_API HWND c_initgraph(int width, int height, COLORREF color = 3419176);//RGB(40, 44, 52);

EASYX_API void c_closegraph();

EASYX_API void c_setaspectratio(float x = 1, float y = 1);

EASYX_API void c_graphdefaults();

EASYX_API void c_setorigin(int x = 0, int y = 0);

//颜色模型;

EASYX_API BYTE c_GetBValue(COLORREF rgb);

EASYX_API BYTE c_GetGValue(COLORREF rgb);

EASYX_API BYTE c_GetRValue(COLORREF rgb);

EASYX_API COLORREF c_HSLtoRGB(float H, float S, float L);

EASYX_API COLORREF c_HSVtoRGB(float H, float S, float V);

EASYX_API COLORREF c_RGB(BYTE byRed, BYTE byGreen, BYTE byBlue);

EASYX_API COLORREF c_RGBtoGRAY(COLORREF rgb);

//图形颜色及样式设置相关函数;

EASYX_API COLORREF c_getbkcolor();

EASYX_API int c_getbkmode();

EASYX_API COLORREF c_getfillcolor();

EASYX_API COLORREF c_getlinecolor();

EASYX_API void c_setbkcolor(COLORREF color = 3419176);//RGB(40, 44, 52);

EASYX_API void c_setbkmode(int mode = TRANSPARENT);

EASYX_API void c_setfillcolor(COLORREF color = 15724527); //RGB(239, 239, 239);

EASYX_API void c_setfillstyle(int style = BS_SOLID, long hatch = NULL, IMAGE *ppattern = NULL);

EASYX_API void c_setlinecolor(COLORREF color = 15724527);//RGB(239, 239, 239);

EASYX_API void c_setlinestyle(int style = PS_SOLID | PS_ENDCAP_ROUND, int thickness = 1, const DWORD *puserstyle = NULL, DWORD userstylecount = 0);

//图形绘制相关函数;
EASYX_API void c_arc(int left, int top, int right, int bottom, double stangle, double endangle);

EASYX_API void c_circle(int x, int y, int radius);

EASYX_API void c_clearcircle(int x, int y, int radius);

EASYX_API void c_clearellipse(int left, int top, int right, int bottom);

EASYX_API void c_clearpie(int left, int top, int right, int bottom, double stangle, double endangle);

EASYX_API void c_clearpolygon(const POINT *points, int num);

EASYX_API void c_clearrectangle(int left, int top, int right, int bottom);

EASYX_API void c_clearroundrect(int left, int top, int right, int bottom, int ellipsewidth, int ellipseheight);

EASYX_API void c_ellipse(int left, int top, int right, int bottom);

EASYX_API void c_fillcircle(int x, int y, int radius);

EASYX_API void c_fillellipse(int left, int top, int right, int bottom);

EASYX_API void c_fillpie(int left, int top, int right, int bottom, double stangle, double endangle);

EASYX_API void c_putpixel(int x, int y, COLORREF color);
