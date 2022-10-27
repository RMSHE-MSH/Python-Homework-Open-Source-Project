//Powered by RMSHE / 2022.10.02;
#pragma once
#include "Universal.h"

#define EASYX_API extern "C" __declspec(dllexport)

//VectorStack(图形矢量堆栈)相关函数;

EASYX_API void c_free_vecstack();

EASYX_API long long int c_size_vecstack();

EASYX_API void c_pop_vecstack();

EASYX_API void c_back_vecstack();

EASYX_API void c_refresh_vecstack();

EASYX_API void c_translation_vecstack(int Vecindex[2], int target[2]);

EASYX_API void c_resize_vecstack(int Vecindex[2], float factor, int Base[2]);

EASYX_API void c_rotate_vecstack(int Vecindex[2], float angle, int Base[2]);

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

EASYX_API void c_setlinestyle(int style = PS_SOLID | PS_ENDCAP_ROUND, float thickness = 1.0, const DWORD *puserstyle = NULL, DWORD userstylecount = 0);

//图形绘制相关函数;
EASYX_API void c_arc(float left, float top, float right, float bottom, float stangle, float endangle);

EASYX_API void c_circle(float x, float y, float radius);

EASYX_API void c_clearcircle(float x, float y, float radius);

EASYX_API void c_clearellipse(float left, float top, float right, float bottom);

EASYX_API void c_clearpie(float left, float top, float right, float bottom, float stangle = 0, float endangle = 2 * PI);

EASYX_API void c_clearpolygon(float pofloats[], int num);

EASYX_API void c_clearrectangle(float left, float top, float right, float bottom);

EASYX_API void c_clearroundrect(float left, float top, float right, float bottom, float ellipsewidth, float ellipseheight);

EASYX_API void c_ellipse(float left, float top, float right, float bottom);

EASYX_API void c_fillcircle(float x, float y, float radius);

EASYX_API void c_fillellipse(float left, float top, float right, float bottom);

EASYX_API void c_fillpie(float left, float top, float right, float bottom, float stangle, float endangle);

EASYX_API void c_fillpolygon(float points[], int num);

EASYX_API void c_fillrectangle(float left, float top, float right, float bottom);

EASYX_API void c_line(float x1, float y1, float x2, float y2);

EASYX_API void c_putpixel(float x, float y);

//图像处理相关函数;

EASYX_API void c_loadimage(const char *path);

//其它函数;

EASYX_API void c_BeginBatchDraw();

EASYX_API void c_EndBatchDraw();

EASYX_API void c_FlushBatchDraw();
