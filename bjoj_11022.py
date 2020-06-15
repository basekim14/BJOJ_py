"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-15
Baekjoon Online Judge Study - 11022(A+B - 8)
"""

from sys import stdin

T = int(stdin.readline())
for i in range(T):
    A, B = map(int, stdin.readline().split())
    print("Case #%d: %d + %d = %d" % (i+1, A, B, A + B))
