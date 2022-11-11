# Powered by RMSHE;
# 2022.11.09;

def verdict(grades: float):
    if 90<=grades<=100:
        return "优秀"
    elif 80<=grades<90:
        return "良好"
    elif 60<=grades<80:
        return "及格"
    elif 60<grades:
        return "不及格"

name = "张三"
print(name + "同学,"+str(verdict(eval(input("输入成绩: ")))))
