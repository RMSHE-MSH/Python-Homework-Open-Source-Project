#pragma once
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include "Universal.h"

#define CUDA_API extern "C" __declspec(dllexport)

CUDA_API void TEST();