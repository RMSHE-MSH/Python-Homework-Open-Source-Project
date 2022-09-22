# Vocabulary Inversion (单词表反相)
# Powered by RMSHE / 2022.09.22
# GitHub Open Source: https://github.com/RMSHE-MSH/Python-Homework-Open-Source-Project
"""----------------------------------------------------------------------------------------------
原理: 对输入的字符串进行正则表达匹配(匹配连续的英文字母),之后每一段连续的英文字母都会被提取出来添加到列表中,
然后对列表中的元素进行反向,最后以空格作为连接符连接列表中的所有单词.
----------------------------------------------------------------------------------------------"""
import re

print(" ".join(list(reversed(re.findall('[a-zA-Z]+', str(input("Please enter string here:\n")))))))
# TestStr: world          the with right All   heaven his        in God
