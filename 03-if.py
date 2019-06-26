
# -*- coding: UTF-8 -*-

# Filename : 03-if.py
# author by : （学员ID)

# 目的:
# 掌握使用 if 语句

# elif 的使用
# 用户输入数字
'''
num = float(input("输入一个数字: "))
if num > 0:
   print("正数")
elif num == 0:
   print("零")
else:
   print("负数")
'''

'''
# Python 判断奇数偶数
# 如果是偶数除于 2 余数为 0
# 如果余数为 1 则为奇数
num = int(input("输入一个整数: "))
if (num % 2) == 0:
    # print("%d 是偶数" % num)
    print("%s 是偶数" % str(num))
    # print("{0} 是偶数".format(num))
else:
    print("%d 是奇数" % num)
    # print("{0} 是奇数".format(num))
'''

# 判断是否为闰年
# 闰年条件：闰年条件, 满足年份模400为0, 或者模4为0但模100不为0.
year = int(input("输入一个年份: "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} 是闰年".format(year))  # 整百年能被400整除的是闰年
        else:
            print("{0} 不是闰年".format(year))
    else:
        print("{0} 是闰年".format(year))  # 非整百年能被4整除的为闰年
else:
    print("{0} 不是闰年".format(year))
