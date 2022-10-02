#include "pch.h"
#include "EasyXGraphicsFunction.h"

void c_cleardevice() { cleardevice(); }

HWND c_initgraph(int width, int height, int flag) {
	HWND hWnd = initgraph(width, height, flag);
	setorigin(0, 0);
	setbkcolor(RGB(30, 30, 30));
	cleardevice();
	setaspectratio(1, 1);
	::setbkmode(TRANSPARENT);
	return hWnd;
}

void c_closegraph() { closegraph(); }

void c_setaspectratio(float x, float y) { setaspectratio(x, y); }

void c_graphdefaults() { graphdefaults(); }

void c_setorigin(int x, int y) { setorigin(x, y); }

BYTE c_GetBValue(COLORREF rgb) { return GetBValue(rgb); }

BYTE c_GetGValue(COLORREF rgb) { return GetGValue(rgb); }

BYTE c_GetRValue(COLORREF rgb) { return GetRValue(rgb); }

COLORREF c_HSLtoRGB(float H, float S, float L) { return HSLtoRGB(H, S, L); }

COLORREF c_HSVtoRGB(float H, float S, float V) { return HSVtoRGB(H, S, V); }

COLORREF c_RGB(BYTE byRed, BYTE byGreen, BYTE byBlue) { return RGB(byRed, byGreen, byBlue); }

void c_putpixel(int x, int y, COLORREF color) { putpixel(x, y, color); }

void c_circle(int x, int y, int radius) { circle(x, y, radius); }