"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-23
Baekjoon Online Judge Study - 1929(sieve of eratosthenes)

"""

def prime_list(n):
    sieve = [True] * (n+1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False

    return [i for i in range(2, n+1) if sieve[i] == True]

M, N = map(int, input().split())
numlist = [i for i in prime_list(N) if i >= M]

for num in numlist:
    print(num)

