"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-01
Baekjoon Online Judge Study - 1065(equidistant sequence)
"""

from sys import stdin

def is_hansu(N):
    if N < 100:
        return True
    
    Nlist = [int(n) for n in str(N)]
    for i in range(len(Nlist) - 2):
        if Nlist[i+1] - Nlist[i] != Nlist[i+2] - Nlist[i+1]:
            return False
    return True

N = int(stdin.readline())
count = 0
for i in range(1, N+1):
    if is_hansu(i):
        count += 1
print(count)
