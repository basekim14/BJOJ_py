# Baekjoon Online Judge Study - 1008
# Author : ㄱㄱㅊ
# Title : A/B
# Date : 20-06-12

from sys import stdin

A, B = map(int, stdin.readline().split())
print(A+B, A-B, A*B, A//B, A%B, sep="\n")
