#pragma once
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include "Universal.h"

#define CUDA_API extern "C" __declspec(dllexport)

//CUDA_API float **GPU_rotate(vector<float> PointStack_X, vector<float> PointStack_Y, float angle, POINT Base);

CUDA_API float **GPU_rotate(float **PointStack, int num, float angle, POINT Base);