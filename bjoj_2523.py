"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-18
Baekjoon Online Judge Study - 2523(print * - 13)
"""

from sys import stdin

N = int(stdin.readline())
for i in range(N):
    print("*" * (i+1)) 
for i in range(N-1, 0, -1):
    print("*" * i)
