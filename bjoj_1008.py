"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-12
Baekjoon Online Judge Study - 1008(A/B)
"""

from sys import stdin

A, B = map(int, stdin.readline().split())
print(A+B, A-B, A*B, A//B, A%B, sep="\n")
