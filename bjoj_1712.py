"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-10
Baekjoon Online Judge Study - 1712(break-even point)
"""

from sys import stdin

A, B, C = map(int, stdin.readline().split())
BEpoint = 0

if C <= B:
    BEpoint = -1
else:
    BEpoint = A // (C-B) + 1

print(BEpoint)
