"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-29
Baekjoon Online Judge Study - 11720(sum of numbers)
"""

from sys import stdin

N = int(stdin.readline())
nums = stdin.readline()[:N]
print(sum([int(v) for v in list(nums)]))
