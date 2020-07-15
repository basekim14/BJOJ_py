"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-15
Baekjoon Online Judge Study - 2869(snail climbing)
"""

from sys import stdin

def climb(A, B, V):
    if A >= V:
        return 1
    
    d = (V - A) // (A - B)
    if (V - A) % (A-B) == 0:
        return d + 1
    else:
        return d + 2

A, B, V = map(int, stdin.readline().split())
print(climb(A, B, V))
