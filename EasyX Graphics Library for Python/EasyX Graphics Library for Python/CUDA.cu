#include "CUDA.cuh"

__global__ void helloGPU() {
	printf("Hello from the GPU.\n");
}

void TEST() {
	helloGPU << <100, 100 >> > ();
	cudaDeviceSynchronize();
}