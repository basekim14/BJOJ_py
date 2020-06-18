"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-18
Baekjoon Online Judge Study - 2446(print * - 9)
"""

from sys import stdin

N = int(stdin.readline())
for i in range(N):
    print(" " * i + "*" * (2 * (N-i) - 1))
for i in range(N-1, 0, -1):
    print(" " * (i-1) + "*" * (2 * (N-i+1) - 1)) 

