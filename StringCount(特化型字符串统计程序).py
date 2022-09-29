# StringCount (特化型字符串统计程序)
# Powered by RMSHE / 2022.09.22
# GitHub Open Source: https://github.com/RMSHE-MSH/Python-Homework-Open-Source-Project
# 原理: 字符串统计的方法一大堆,我这里是利用了ASCII区间对应的字符类型;

Count = {'Space': 0, 'Lowercase': 0, 'Uppercase': 0, 'Number': 0}
for i in str(input("Please enter any string here:\n")):
    if ord(i) == 32:
        Count['Space'] += 1  # 空格的ASCII值为32;
    elif 97 <= ord(i) <= 122:
        Count['Lowercase'] += 1  # 小写怎么的ASCII值在[97,122]区间;
    elif 65 <= ord(i) <= 90:
        Count['Uppercase'] += 1  # 大写怎么的ASCII值在[65,90]区间;
    elif 48 <= ord(i) <= 57:
        Count['Number'] += 1  # 数字写怎么的ASCII值在[48,57]区间;

print(Count)  # TestStr: God's in his heaven, All's right with the world. GAATTC-299792458-3.1415926535897932384626433832795
