"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-12
Baekjoon Online Judge Study - 10430(multiplication)
"""

from sys import stdin

A, B = [stdin.readline().strip() for i in range(2)]
Bnums = [int(Bnum) for Bnum in list(B)]
A, B = int(A), int(B)

for Bnum in reversed(Bnums):
    print(A * Bnum)
print(A * B)
