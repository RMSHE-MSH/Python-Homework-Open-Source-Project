#include "CUDA.cuh"

void GPU_Device_Initialize() {
	int gpuCount = -1;
	cudaGetDeviceCount(&gpuCount);
	//printf("gpuCount: %d\n", gpuCount);
	if (gpuCount <= 0)printf("ERROR: NO CUDA GPU\n");

	cudaSetDevice(gpuCount - 1);
}

//__global__ void rotate_X(float *PointStack_X_GPU, float angle, POINT Base) {
//	int i = threadIdx.x;
//	PointStack_X_GPU[i] = PointStack_X_GPU[i] * cos(angle) - PointStack_X_GPU[i] * sin(angle) + Base.x * (1 - cos(angle)) + Base.y * sin(angle);
//}
//__global__ void rotate_Y(float *PointStack_Y_GPU, float angle, POINT Base) {
//	int i = threadIdx.x;
//	PointStack_Y_GPU[i] = PointStack_Y_GPU[i] * sin(angle) + PointStack_Y_GPU[i] * cos(angle) + Base.y * (1 - cos(angle)) - Base.x * sin(angle);
//}
//
//float **GPU_rotate(vector<float> PointStack_X, vector<float> PointStack_Y, float angle, POINT Base) {
//	GPU_Device_Initialize();
//
//	//init data;
//	float *PointStack_X_CPU = new float[PointStack_X.size()];
//	float *PointStack_Y_CPU = new float[PointStack_Y.size()];
//
//	float *PointStack_X_GPU = nullptr;
//	float *PointStack_Y_GPU = nullptr;
//
//	for (int i = 0; i < PointStack_X.size(); ++i) PointStack_X_CPU[i] = PointStack_X[i];
//	for (int i = 0; i < PointStack_Y.size(); ++i) PointStack_Y_CPU[i] = PointStack_Y[i];
//
//	//new space;
//	cudaMalloc((void **)&PointStack_X_GPU, PointStack_X.size() * sizeof(float));
//	cudaMalloc((void **)&PointStack_Y_GPU, PointStack_Y.size() * sizeof(float));
//
//	//copy data CPU -> GPU;
//	cudaMemcpy(PointStack_X_GPU, PointStack_X_CPU, PointStack_X.size() * sizeof(float), cudaMemcpyHostToDevice);
//	cudaMemcpy(PointStack_Y_GPU, PointStack_Y_CPU, PointStack_Y.size() * sizeof(float), cudaMemcpyHostToDevice);
//
//	//do;
//	int threadnum = 1024;
//	int blocknum = 1024;
//
//	rotate_X << <blocknum, threadnum >> > (PointStack_X_GPU, angle, Base);
//	rotate_Y << <blocknum, threadnum >> > (PointStack_Y_GPU, angle, Base);
//
//	//copy data GPU -> CPU;
//	cudaMemcpy(PointStack_X_CPU, PointStack_X_GPU, PointStack_X.size() * sizeof(float), cudaMemcpyDeviceToHost);
//	cudaMemcpy(PointStack_Y_CPU, PointStack_Y_GPU, PointStack_Y.size() * sizeof(float), cudaMemcpyDeviceToHost);
//
//	float **PointStack_GPU = new float *[PointStack_X.size()] { NULL };
//	for (int i = 0; i < PointStack_X.size(); ++i) {
//		PointStack_GPU[i] = new float[2] {NULL};
//
//		PointStack_GPU[i][0] = PointStack_X_CPU[i];
//		PointStack_GPU[i][1] = PointStack_Y_CPU[i];
//	}
//
//	//free;
//	cudaFree(PointStack_X_GPU); delete[]PointStack_X_CPU;
//	cudaFree(PointStack_Y_GPU); delete[]PointStack_Y_CPU;
//
//	/*for (int i = 0; i < PointStack_X.size(); ++i)cout << PointStack_X_CPU[i] << endl;
//	cout << endl;
//	for (int i = 0; i < PointStack_Y.size(); ++i)cout << PointStack_Y_CPU[i] << endl;*/
//
//	//cudaDeviceReset();
//
//	return PointStack_GPU;
//}

__global__ void rotate(float **PointStack_GPU, float angle, POINT Base) {
	int i = threadIdx.x;
}

float **GPU_rotate(float **PointStack, int num, float angle, POINT Base) {
	GPU_Device_Initialize();

	//init data;
	float **PointStack_GPU = nullptr;
	float **PointStack_CPU = nullptr;

	//new space;
	size_t pitch;
	cudaMallocPitch((void **)&PointStack_GPU, &pitch, width * sizeof(float), height);
	//cudaMallocPitch((void **)&PointStack_GPU, num * sizeof(float));

	//copy data CPU -> GPU;
	cudaMemcpy(PointStack_GPU, PointStack, num * sizeof(float), cudaMemcpyHostToDevice);

	//do;
	rotate << <1, 1024 >> > (PointStack_GPU, angle, Base);

	//copy data GPU -> CPU;
	cudaMemcpy(PointStack_CPU, PointStack_GPU, num * sizeof(float), cudaMemcpyDeviceToHost);

	//free;
	cudaFree(PointStack_GPU);

	return nullptr;
}