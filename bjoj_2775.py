"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-17
Baekjoon Online Judge Study - 2775(TPOWS)
"""

from sys import stdin

def count_member(k, n):
    if k == 0:
        return n

    if k == 1:
        return n * (n + 1) // 2
    
    base = [i for i in range(1, n+1)]
    for _ in range(k):
        for i in range(1, n):
            base[i] += base[i-1]
    return base[-1]

for _ in range(int(stdin.readline())):
    k = int(stdin.readline())
    n = int(stdin.readline())
    print(count_member(k, n))
