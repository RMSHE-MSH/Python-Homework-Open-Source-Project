# Powered by RMSHE;
# 2022.11.09;
import time
import random
hits=0
pi=0
DARTS=3000*3000
start=time.perf_counter()
for i in range(DARTS):
    x,y=random.random(),random.random()
    dist=pow(x ** 2+y**2,0.5)
    if dist <= 1.0:
        hits+=1
pi=4*(hits/DARTS)
radius=eval(input("请输入圆的半径: "))
print(f"圆的面积为: {pi * (radius * radius)}")

get_msg = 1