"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-13
Baekjoon Online Judge Study - 14681(quadrant section)
"""

from sys import stdin

x = int(stdin.readline())
y = int(stdin.readline())

if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)
