"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-22
Baekjoon Online Judge Study - 1546(average)
"""

from sys import stdin

N = int(stdin.readline())
scores = list(map(int, stdin.readline().split()))
M = max(scores)
print(sum([score/M*100 for score in scores]) / len(scores))
