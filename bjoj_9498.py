# Baekjoon Online Judge Study - 9498
# Author : ㄱㄱㅊ
# Title : test score
# Date : 20-06-13

from sys import stdin

score = int(stdin.readline())
if 100 >= score >= 90: print("A")
elif 90 > score >= 80: print("B")
elif 80 > score >= 70: print("C")
elif 70 > score >= 60: print("D")
else: print("F")
