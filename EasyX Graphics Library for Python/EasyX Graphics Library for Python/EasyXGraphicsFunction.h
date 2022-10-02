#pragma once
#include "Universal.h"

#define DLLTEST_API extern "C" __declspec(dllexport)

DLLTEST_API HWND c_initgraph(int width, int height, int flag = EW_SHOWCONSOLE);

DLLTEST_API void c_circle(int x, int y, int radius);
