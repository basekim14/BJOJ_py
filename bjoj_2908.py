"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-04
Baekjoon Online Judge Study - 2908(sang su)
"""

from sys import stdin

A, B = [int("".join(reversed(list(num)))) for num in stdin.readline().split()]
print(A if A > B else B)
