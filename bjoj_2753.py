# Baekjoon Online Judge Study - 2753
# Author : ㄱㄱㅊ
# Title : leap year
# Date : 20-06-13

from sys import stdin

year = int(stdin.readline())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(1)
else:
    print(0)
