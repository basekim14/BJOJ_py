"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-20
Baekjoon Online Judge Study - 2557(number of numbers)
"""

from sys import stdin

A, B, C = [int(stdin.readline()) for _ in range(3)]
result = list(map(int, str(A * B * C)))
for i in range(10):
    print(result.count(i))
