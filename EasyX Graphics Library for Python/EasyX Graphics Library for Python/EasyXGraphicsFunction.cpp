#include "pch.h"
#include "EasyXGraphicsFunction.h"

void c_cleardevice() { cleardevice(); }

HWND c_initgraph(int width, int height) {
	HWND hWnd = initgraph(width, height, EW_SHOWCONSOLE);
	setorigin(0, 0);
	setbkcolor(RGB(40, 44, 52));
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

COLORREF c_RGBtoGRAY(COLORREF rgb) { return RGBtoGRAY(rgb); }

COLORREF c_getbkcolor() { return getbkcolor(); }

int c_getbkmode() { return getbkmode(); }

COLORREF c_getfillcolor() { return getfillcolor(); }

COLORREF c_getlinecolor() { return getlinecolor(); }

void c_setbkcolor(COLORREF color) { setbkcolor(color); }

void c_setbkmode(int mode) { setbkmode(mode); }

void c_setfillcolor(COLORREF color) { setfillcolor(color); }

void c_setfillstyle(int style, long hatch, IMAGE *ppattern) { setfillstyle(style, hatch, ppattern); }

void c_setlinecolor(COLORREF color) { setlinecolor(color); }

void c_setlinestyle(int style, int thickness, const DWORD *puserstyle, DWORD userstylecount) { setlinestyle(style, thickness, puserstyle, userstylecount); }

void c_arc(int left, int top, int right, int bottom, double stangle, double endangle) { arc(left, top, right, bottom, stangle, endangle); }

void c_circle(int x, int y, int radius) { circle(x, y, radius); }

void c_clearcircle(int x, int y, int radius) { clearcircle(x, y, radius); }

void c_clearellipse(int left, int top, int right, int bottom) { clearellipse(left, top, right, bottom); }

void c_clearpie(int left, int top, int right, int bottom, double stangle, double endangle) { clearpie(left, top, right, bottom, stangle, endangle); }

void c_clearpolygon(const POINT *points, int num) { clearpolygon(points, num); }

void c_clearrectangle(int left, int top, int right, int bottom) { clearrectangle(left, top, right, bottom); }

void c_clearroundrect(int left, int top, int right, int bottom, int ellipsewidth, int ellipseheight) { clearroundrect(left, top, right, bottom, ellipsewidth, ellipseheight); }

void c_ellipse(int left, int top, int right, int bottom) { ellipse(left, top, right, bottom); }

void c_fillcircle(int x, int y, int radius) { fillcircle(x, y, radius); }

void c_fillellipse(int left, int top, int right, int bottom) { fillellipse(left, top, right, bottom); }

void c_fillpie(int left, int top, int right, int bottom, double stangle, double endangle) { fillpie(left, top, right, bottom, stangle, endangle); }

void c_putpixel(int x, int y, COLORREF color) { putpixel(x, y, color); }