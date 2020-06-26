"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-26
Baekjoon Online Judge Study - 4344(over the average)
"""

from sys import stdin

C = int(stdin.readline())
cases = [list(map(int, stdin.readline().split())) for _ in range(C)]

for case in cases:
    n, scores = case[0], case[1:]
    average = sum(scores) / n
    result = round(len([v for v in scores if v > average]) / len(scores) * 100, 3)
    print("%.3f%%" % result)
