"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-08-06
Baekjoon Online Judge Study - 3036(ring)
"""

from math import gcd

N = int(input())
rlist = list(map(int, input().split()))
for r in rlist[1:N]:
    g = gcd(rlist[0], r)
    print(rlist[0]//g, r//g, sep="/")
