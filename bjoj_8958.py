"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-23
Baekjoon Online Judge Study - 8958(OX quiz)
"""

from sys import stdin

oxlist = [stdin.readline().rstrip() for _ in range(int(stdin.readline()))]
for ox in oxlist:
    print(sum([((len(v) + 1) * len(v) // 2) for v in [v for v in ox.split("X") if v]]))
