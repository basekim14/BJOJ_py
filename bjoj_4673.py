"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-01
Baekjoon Online Judge Study - 4673(self numbers)
"""

def find_selfnums(n):
    dn = n + sum([int(v) for v in str(n)])
    try:
        if not boolist[dn]:
            return
        boolist[dn] = False
        find_selfnums(dn)
    except IndexError:
        return
    
MAX = 10000
boolist = [None] + [True] * MAX

for i in range(1, MAX+1):
    find_selfnums(i)

for i in range(1, MAX+1):
    if boolist[i]:
        print(i)
