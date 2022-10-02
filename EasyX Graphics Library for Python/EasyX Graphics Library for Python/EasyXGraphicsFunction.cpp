#include "pch.h"
#include "EasyXGraphicsFunction.h"

HWND c_initgraph(int width, int height, int flag) {
	HWND hWnd = initgraph(width, height, flag);
	setorigin(0, 0);
	//setbkcolor(RGB(241, 243, 245));
	setbkcolor(RGB(30, 30, 30));
	cleardevice();
	setaspectratio(1, 1);
	::setbkmode(TRANSPARENT);
	return hWnd;
}

void c_circle(int x, int y, int radius) { circle(x, y, radius); }