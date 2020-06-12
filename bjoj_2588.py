# Baekjoon Online Judge Study - 10430
# Author : ㄱㄱㅊ
# Title : Remainder
# Date : 20-06-12

from sys import stdin

A, B = [stdin.readline().strip() for i in range(2)]
Bnums = [int(Bnum) for Bnum in list(B)]
A, B = int(A), int(B)

for Bnum in reversed(Bnums):
    print(A * Bnum)
print(A * B)
