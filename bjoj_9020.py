"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-25
Baekjoon Online Judge Study - 9020(goldbach's conjecture)
"""

LEN = 10000
sieve = [False] + [True] * LEN
sieve[1] = False
m = int(LEN ** 0.5)
for i in range(2, m+1):
    if sieve[i] == True:
        for j in range(i+i, LEN+1, i):
            sieve[j] = False

for _ in range(int(input())):
    n = int(input())
    if n == 4:
        print(2, 2)
        
    for a in range(n//2 + (0 if n//2%2 else -1), -1, -2):
        b = n - a
        if sieve[a] and sieve[b]:
            print(a, b)
            break



