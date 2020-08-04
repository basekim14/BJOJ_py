"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-08-03
Baekjoon Online Judge Study - 11653(prime factorization)
"""

N = int(input())
i = 2

while i <= int(N**0.5):
    if N % i == 0:
        N //= i
        print(i)
    else:
        i += 1
if N > 1:
    print(N)
