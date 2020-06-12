# Baekjoon Online Judge Study - 10430
# Author : ㄱㄱㅊ
# Title : Remainder
# Date : 20-06-12

from sys import stdin

A, B, C = map(int, stdin.readline().split())
print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep="\n")
