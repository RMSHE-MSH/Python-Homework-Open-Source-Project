# Powered by RMSHE;
def temperature_conversion(Input, keep_decimals):
    OUTPUT = ""
    if Input[0:-1].isdigit() and (Input[-1] in ['C', 'c', 'F', 'f']) == True:
        if Input[-1] in ['F', 'f']:
            OUTPUT = str((eval(Input[0:-1]) - 32) * 0.5555555555555556) + "C"
        else:
            OUTPUT = str(eval(Input[0:-1]) * 1.8 + 32) + "F"

        if keep_decimals == 0:
            return str(OUTPUT).split('.')[0] + str(OUTPUT).split('.')[1][:keep_decimals] + OUTPUT[-1]
        else:
            if keep_decimals > (len(OUTPUT) - OUTPUT.index('.') - 2):
                return str(OUTPUT).split('.')[0] + "." + str(OUTPUT).split('.')[1][:(len(OUTPUT) - OUTPUT.index('.') - 2)] + OUTPUT[-1]
            else:
                return str(OUTPUT).split('.')[0] + "." + str(OUTPUT).split('.')[1][:keep_decimals] + OUTPUT[-1]

    elif (Input[1:-1] + Input[-1]).isdigit() and Input[0] in ['C', 'c', 'F', 'f']:
        if Input[0] in ['F', 'f']:
            OUTPUT = str((eval(Input[1:-1] + Input[-1]) - 32) * 0.5555555555555556) + "C"
        else:
            OUTPUT = str(eval(Input[1:-1] + Input[-1]) * 1.8 + 32) + "F"

        if keep_decimals == 0:
            return str(OUTPUT).split('.')[0] + str(OUTPUT).split('.')[1][:keep_decimals] + OUTPUT[-1]
        else:
            if keep_decimals > (len(OUTPUT) - OUTPUT.index('.') - 2):
                return str(OUTPUT).split('.')[0] + "." + str(OUTPUT).split('.')[1][:(len(OUTPUT) - OUTPUT.index('.') - 2)] + OUTPUT[-1]
            else:
                return str(OUTPUT).split('.')[0] + "." + str(OUTPUT).split('.')[1][:keep_decimals] + OUTPUT[-1]

    else:
        return "input format error"


# temperature_conversion("在此填入待转换数据",输出结果需要保留的小数位数);
# 在此填入待转换数据的格式可以是:" C25, 25C, c25, 25c, F77, f77, 77F, 77f";
# print(temperature_conversion2(input("Please enter temperature value & unit: "), 0));

# 以下是不同输入格式的演示;
print(temperature_conversion("25c", 0))
print(temperature_conversion("25C", 0))
print(temperature_conversion("c25", 0))
print(temperature_conversion("C25", 0))

print(temperature_conversion("26c", 1))
print(temperature_conversion("26C", 2))
print(temperature_conversion("c26", 3))
print(temperature_conversion("C26", 4))

print(temperature_conversion("25f", 0))
print(temperature_conversion("25F", 0))
print(temperature_conversion("f25", 0))
print(temperature_conversion("F25", 0))

print(temperature_conversion("26f", 1))
print(temperature_conversion("26F", 2))
print(temperature_conversion("f26", 3))
print(temperature_conversion("F26", 4))
