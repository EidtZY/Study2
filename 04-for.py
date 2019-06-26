
# -*- coding: UTF-8 -*-

# Filename : 04-for.py
# author by : （学员ID)

# 目的:
# 掌握使用for语句

# 最简单的 for
for i in range(1, 10, 2) :
    print(i)


# 输出指定范围内的素数
# take input from the user
print("-----华丽分割线-----")
print("输出指定范围内所有整数：")
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))
for num in range(lower, upper + 1):
    print(num)


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
