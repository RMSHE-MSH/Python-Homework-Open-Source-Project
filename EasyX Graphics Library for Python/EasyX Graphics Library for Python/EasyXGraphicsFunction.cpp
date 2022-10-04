#include "pch.h"
#include "EasyXGraphicsFunction.h"

//VectorStack图形矢量堆栈;
typedef struct POINT_COLORREF { COLORREF lineColor; COLORREF fillColor; }POINT_COLORREF;
typedef struct LINE_STYLE { int Style; int thickness; }LINE_STYLE;
typedef struct FILL_STYLE { int Style; long hatch; }FILL_STYLE;
LINE_STYLE PresentLineStyle = { NULL,NULL };
FILL_STYLE PresentFillStyle = { NULL,NULL };

typedef struct POINT_STYLE { LINE_STYLE lineStyle; FILL_STYLE FillStyle; }POINT_STYLE;

typedef struct VECSTACK { int TypeStack; POINT PointStack; int ShapeStack; POINT_COLORREF ColorStack; POINT_STYLE StyleStack; }VECSTACK;

class VectorStack {
private:
	long long int Size = -1;

	vector<int> TypeStack;
	vector<POINT> PointStack;
	vector<int> ShapeStack;
	vector<POINT_COLORREF> ColorStack;
	vector<POINT_STYLE> StyleStack;
public:
	bool VecStackPow = true;	//激活矢量堆栈(总开关);
	bool ReadOnly = false;		//矢量堆栈只读开关;

	long long int size() { return Size; }

	void push(int Type, POINT Point, int Shape) {
		if (VecStackPow == true && ReadOnly == false) {
			TypeStack.push_back(Type);
			PointStack.push_back(Point);
			ShapeStack.push_back(Shape);
			ColorStack.push_back({ getlinecolor(),getfillcolor() });
			StyleStack.push_back({ PresentLineStyle,PresentFillStyle });

			++Size;
		}
	}

	VECSTACK pop() {
		if (VecStackPow == true && ReadOnly == false) {
			VECSTACK pop_data = { TypeStack[Size],PointStack[Size],ShapeStack[Size],ColorStack[Size],StyleStack[Size] };

			TypeStack.pop_back();
			PointStack.pop_back();
			ShapeStack.pop_back();
			ColorStack.pop_back();
			StyleStack.pop_back();

			--Size;

			return pop_data;
		}
	}

	vector<VECSTACK> back() {
		if (VecStackPow == true && ReadOnly == false) {
			pop();

			vector<VECSTACK> BackStack;
			for (int i = 0; i <= Size; ++i)BackStack.push_back({ TypeStack[i], PointStack[i], ShapeStack[i], ColorStack[i], StyleStack[i] });

			return BackStack;
		}
	}
}VecStack;

void c_pop_vecstack() {
	VECSTACK pop_data = VecStack.pop();

	setlinecolor(pop_data.ColorStack.lineColor); setfillcolor(pop_data.ColorStack.fillColor);
	setlinestyle(pop_data.StyleStack.lineStyle.Style, pop_data.StyleStack.lineStyle.thickness);
	setfillstyle(pop_data.StyleStack.FillStyle.Style, pop_data.StyleStack.FillStyle.hatch);

	cleardevice();
	if (pop_data.TypeStack == CIRCLE) {
		circle(pop_data.PointStack.x, pop_data.PointStack.y, pop_data.ShapeStack);
	}
}

void c_back_vecstack() {
	vector<VECSTACK> back_data = VecStack.back();

	cleardevice();
	for (int i = 0; i <= VecStack.size(); ++i) {
		setlinecolor(back_data[i].ColorStack.lineColor); setfillcolor(back_data[i].ColorStack.fillColor);
		setlinestyle(back_data[i].StyleStack.lineStyle.Style, back_data[i].StyleStack.lineStyle.thickness);
		setfillstyle(back_data[i].StyleStack.FillStyle.Style, back_data[i].StyleStack.FillStyle.hatch);

		if (back_data[i].TypeStack == CIRCLE) {
			circle(back_data[i].PointStack.x, back_data[i].PointStack.y, back_data[i].ShapeStack);
		}
	}
}

void c_cleardevice() { cleardevice(); }

HWND c_initgraph(int width, int height, COLORREF color) {
	HWND hWnd = initgraph(width, height, EW_SHOWCONSOLE);
	setorigin(0, 0);
	setbkcolor(color);

	if (color < RGB(128, 128, 128)) {
		setlinecolor(RGB(239, 239, 239));
		setfillcolor(RGB(97, 175, 239));
	} else {
		setlinecolor(RGB(45, 45, 45));
		setfillcolor(RGB(47, 84, 115));
	}

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

void c_setfillstyle(int style, long hatch, IMAGE *ppattern) {
	setfillstyle(style, hatch, ppattern);
	PresentFillStyle = { style ,hatch };
}

void c_setlinecolor(COLORREF color) { setlinecolor(color); }

void c_setlinestyle(int style, int thickness, const DWORD *puserstyle, DWORD userstylecount) {
	setlinestyle(style, thickness, puserstyle, userstylecount);
	PresentLineStyle = { style ,thickness };
}

void c_arc(int left, int top, int right, int bottom, double stangle, double endangle) { arc(left, top, right, bottom, stangle, endangle); }

void c_circle(int x, int y, int radius) { circle(x, y, radius); VecStack.push(CIRCLE, { x,y }, radius); }

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