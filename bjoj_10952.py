"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-16
Baekjoon Online Judge Study - 10952(A+B - 5)
"""

from sys import stdin

while  True:
    A, B = map(int, stdin.readline().split())
    if A + B == 0: break
    else: print(A + B)

