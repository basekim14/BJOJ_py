"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-22
Baekjoon Online Judge Study - 3052(remainder)
"""

from sys import stdin

mylist = [int(stdin.readline()) % 42 for _ in range(10)]
print(len(set(mylist)))
