"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-16
Baekjoon Online Judge Study - 2439(print * - 2)
"""

from sys import stdin

n = int(stdin.readline())
for i in range(1, n + 1):
    print(("*" * i).rjust(n))
