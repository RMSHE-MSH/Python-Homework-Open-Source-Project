#include "pch.h"
#include "EasyXGraphicsFunction.h"
#include "CUDA.cuh"

//VectorStack图形矢量堆栈;
typedef struct POINT_COLORREF { COLORREF lineColor; COLORREF fillColor; }POINT_COLORREF;
typedef struct LINE_STYLE { int Style; int thickness; }LINE_STYLE;
typedef struct FILL_STYLE { int Style; long hatch; }FILL_STYLE;
LINE_STYLE PresentLineStyle = { NULL,NULL };
FILL_STYLE PresentFillStyle = { NULL,NULL };

typedef struct POINT_STYLE { LINE_STYLE lineStyle; FILL_STYLE FillStyle; }POINT_STYLE;

typedef struct VECSTACK { int TypeStack; vector<POINT> PointStack; vector<double> ShapeStack; POINT_COLORREF ColorStack; POINT_STYLE StyleStack; }VECSTACK;

class VectorStack {
private:
	long long int Size = -1;

	vector<VECSTACK> VEC_STACK;
public:
	bool VecStackPow = true;	//激活矢量堆栈(总开关);
	bool ReadOnly = false;		//矢量堆栈只读开关;

	long long int size() { return Size; }

	void push(int Type, vector<POINT> Point, vector<double> Shape) {
		if (VecStackPow == true && ReadOnly == false) {
			VEC_STACK.push_back({ Type ,Point ,Shape ,{ getlinecolor(),getfillcolor() } ,{ PresentLineStyle,PresentFillStyle } });

			++Size;
		}
	}

	VECSTACK pop() {
		if (VecStackPow == true && ReadOnly == false && Size != -1) {
			VECSTACK pop_data = VEC_STACK[Size];

			VEC_STACK.pop_back();

			--Size; return pop_data;
		}
		return {};
	}

	vector<VECSTACK> back() {
		if (VecStackPow == true && ReadOnly == false) { pop(); return VEC_STACK; }
		/*vector<VECSTACK> BackStack;
			for (int i = 0; i <= Size; ++i)BackStack.push_back(VEC_STACK[i]);

			vector<VECSTACK> BackStack = { VEC_STACK.begin(),VEC_STACK.end() };
			*/
		return {};
	}

	vector<VECSTACK> clone(unsigned long long int begin = 0, unsigned long long int end = NULL) {
		if (VecStackPow == true) {
			if (end == NULL || end > Size)end = Size;

			vector<VECSTACK> clone_block; copy(VEC_STACK.begin() + begin, VEC_STACK.begin() + end, clone_block.begin());

			return clone_block;
		}
		return {};
	}
}VecStack;

void c_pop_vecstack() {
	VECSTACK pop_data = VecStack.pop();

	setlinecolor(pop_data.ColorStack.lineColor); setfillcolor(pop_data.ColorStack.fillColor);
	setlinestyle(pop_data.StyleStack.lineStyle.Style, pop_data.StyleStack.lineStyle.thickness);
	setfillstyle(pop_data.StyleStack.FillStyle.Style, pop_data.StyleStack.FillStyle.hatch);

	cleardevice();
	switch (pop_data.TypeStack) {
		case ARC:
			arc(pop_data.PointStack[0].x, pop_data.PointStack[0].y, pop_data.PointStack[1].x, pop_data.PointStack[1].y, pop_data.ShapeStack[0], pop_data.ShapeStack[1]); break;
		case CIRCLE:
			circle(pop_data.PointStack[0].x, pop_data.PointStack[0].y, pop_data.ShapeStack[0]); break;
		case CL_CIRCLE:
			clearcircle(pop_data.PointStack[0].x, pop_data.PointStack[0].y, pop_data.ShapeStack[0]); break;
		case CL_ELLIPSE:
			clearellipse(pop_data.PointStack[0].x, pop_data.PointStack[0].y, pop_data.PointStack[1].x, pop_data.PointStack[1].y); break;
		case CL_PIE:
			clearpie(pop_data.PointStack[0].x, pop_data.PointStack[0].y, pop_data.PointStack[1].x, pop_data.PointStack[1].y, pop_data.ShapeStack[0], pop_data.ShapeStack[1]); break;
		case PIXEL:
			putpixel(pop_data.PointStack[0].x, pop_data.PointStack[0].y, pop_data.ColorStack.fillColor); break;
		default:
			break;
	}
}

void c_back_vecstack() {
	vector<VECSTACK> back_data = VecStack.back();

	cleardevice();
	for (auto iterator = back_data.begin(); iterator < back_data.end(); ++iterator) {
		setlinecolor((*iterator).ColorStack.lineColor); setfillcolor((*iterator).ColorStack.fillColor);
		setlinestyle((*iterator).StyleStack.lineStyle.Style, (*iterator).StyleStack.lineStyle.thickness);
		setfillstyle((*iterator).StyleStack.FillStyle.Style, (*iterator).StyleStack.FillStyle.hatch);

		switch ((*iterator).TypeStack) {
			case ARC:
				arc((*iterator).PointStack[0].x, (*iterator).PointStack[0].y, (*iterator).PointStack[1].x, (*iterator).PointStack[1].y, (*iterator).ShapeStack[0], (*iterator).ShapeStack[1]); break;
			case CIRCLE:
				circle((*iterator).PointStack[0].x, (*iterator).PointStack[0].y, (*iterator).ShapeStack[0]); break;
			case CL_CIRCLE:
				clearcircle((*iterator).PointStack[0].x, (*iterator).PointStack[0].y, (*iterator).ShapeStack[0]); break;
			case CL_ELLIPSE:
				clearellipse((*iterator).PointStack[0].x, (*iterator).PointStack[0].y, (*iterator).PointStack[1].x, (*iterator).PointStack[1].y); break;
			case CL_PIE:
				clearpie((*iterator).PointStack[0].x, (*iterator).PointStack[0].y, (*iterator).PointStack[1].x, (*iterator).PointStack[1].y, (*iterator).ShapeStack[0], (*iterator).ShapeStack[1]); break;
			case CL_POLYGON: {
				POINT *pts = new POINT[(*iterator).PointStack.size()];

				for (int j = 0; j < (*iterator).PointStack.size(); ++j) pts[j] = (*iterator).PointStack[j];

				clearpolygon(pts, int((*iterator).ShapeStack[0]));  delete[]pts; break; }
			case PIXEL:
				putpixel((*iterator).PointStack[0].x, (*iterator).PointStack[0].y, (*iterator).ColorStack.fillColor); break;
			default:
				break;
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

//图形绘制相关函数;

void c_arc(int left, int top, int right, int bottom, double stangle, double endangle) {
	arc(left, top, right, bottom, stangle, endangle);
	VecStack.push(ARC, { {left,top},{ right, bottom} }, { stangle ,endangle });
}

void c_circle(int x, int y, int radius) { circle(x, y, radius); VecStack.push(CIRCLE, { { x,y } }, { double(radius) }); }

void c_clearcircle(int x, int y, int radius) { clearcircle(x, y, radius); VecStack.push(CL_CIRCLE, { { x,y } }, { double(radius) }); }

void c_clearellipse(int left, int top, int right, int bottom) {
	clearellipse(left, top, right, bottom);
	VecStack.push(CL_ELLIPSE, { {left,top},{ right, bottom} }, { NULL,NULL });
}

void c_clearpie(int left, int top, int right, int bottom, double stangle, double endangle) {
	clearpie(left, top, right, bottom, stangle, endangle);
	VecStack.push(CL_PIE, { {left,top},{ right, bottom} }, { stangle ,endangle });
}

void c_clearpolygon(int points[], int num) {
	int _num = int(0.5 * num); clearpolygon((POINT *)points, _num);

	vector<POINT> _points; for (int i = 0; i < num; i += 2) _points.push_back({ points[i],points[i + 1] });

	VecStack.push(CL_POLYGON, _points, { (double)_num });
}

void c_clearrectangle(int left, int top, int right, int bottom) { clearrectangle(left, top, right, bottom); }

void c_clearroundrect(int left, int top, int right, int bottom, int ellipsewidth, int ellipseheight) { clearroundrect(left, top, right, bottom, ellipsewidth, ellipseheight); }

void c_ellipse(int left, int top, int right, int bottom) { ellipse(left, top, right, bottom); }

void c_fillcircle(int x, int y, int radius) { fillcircle(x, y, radius); }

void c_fillellipse(int left, int top, int right, int bottom) { fillellipse(left, top, right, bottom); }

void c_fillpie(int left, int top, int right, int bottom, double stangle, double endangle) { fillpie(left, top, right, bottom, stangle, endangle); }

void c_putpixel(int x, int y) { putpixel(x, y, getfillcolor()); VecStack.push(PIXEL, { { x,y } }, { NULL }); }

//其它函数;

void c_BeginBatchDraw() { BeginBatchDraw(); }

void c_EndBatchDraw() { EndBatchDraw(); }

void c_FlushBatchDraw() { FlushBatchDraw(); }