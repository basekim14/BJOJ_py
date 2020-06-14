# Baekjoon Online Judge Study - 2739
# Author : ㄱㄱㅊ
# Title : multiplication table
# Date : 20-06-14

from sys import stdin

N = int(stdin.readline())
for i in range(1, 10):
    print(N, "*", i, "=", N*i)
