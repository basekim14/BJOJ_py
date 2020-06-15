"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-14
Baekjoon Online Judge Study - 2739(multiplication table)
"""

from sys import stdin

N = int(stdin.readline())
for i in range(1, 10):
    print(N, "*", i, "=", N*i)
