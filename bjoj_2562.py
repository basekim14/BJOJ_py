"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-20
Baekjoon Online Judge Study - 2562(max value)
"""

from sys import stdin

mylist = [int(stdin.readline()) for _ in range(9)]
print(max(mylist), mylist.index(max(mylist)) + 1, sep="\n")

