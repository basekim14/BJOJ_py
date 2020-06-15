"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-15
Baekjoon Online Judge Study - 11021(A+B - 7)
"""

from sys import stdin

T = int(stdin.readline())
for i in range(T):
    print("Case #%d: %d" % (i+1, sum(map(int, stdin.readline().split()))))
