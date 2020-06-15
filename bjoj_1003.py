"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-10
Baekjoon Online Judge Study - 1003(fibonacci)
"""

import sys

fibocount = [[1, 0], [0, 1]] + [[0, 0]] * 39

def get_fibocount(n):
    if sum(fibocount[n]):
        return fibocount[n]
    else:
        a = (fibocount[n-1] if sum(fibocount[n-1]) else get_fibocount(n-1)).copy()
        b = (fibocount[n-2] if sum(fibocount[n-2]) else get_fibocount(n-2)).copy()
        fibocount[n] = [x+y for x, y in zip(a, b)]
        return fibocount[n]
        
T = int(sys.stdin.readline())
Nlist = []
for i in range(T):
    Nlist.append(int(sys.stdin.readline()))

for N in Nlist:
    res = get_fibocount(N)
    print(res[0], res[1])
    

"""
import sys
...
list(map(int, sys.stdin.readline().split()))


==

list(map(int, input().split()))

"""
