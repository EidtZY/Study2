# -*- coding: UTF-8 -*-

# Filename : 01-string.py
# author by : （学员ID)

# 目的:
# 掌握字符串的一些常用变换方式
# 掌握字符串的简单运算和判断
# 用户输入两串文字后合并输出
# 注：input() 返回一个字符串
# 输出指定范围内的素数
# take input from the user
print("-----华丽分割线-----")
print("输出指定范围内的素数：")
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))

for num in range(lower, upper + 1):
    # 素数大于 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
