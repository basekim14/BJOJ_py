"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-24
Baekjoon Online Judge Study - 4948(bertrand's postulate)
"""
LEN = 2 * 123456
sieve = [False] + [True] * LEN
sieve[1] = False
m = int(LEN ** 0.5)
for i in range(2, m+1):
    if sieve[i] == True:
        for j in range(i+i, LEN+1, i):
            sieve[j] = False

while True:
    t = int(input())
    if t == 0:
        break
    elif t == 1:
        print(1)
    else:
        print(sum(sieve[t + 1:2 * t + 1]))

"""
# runtime error
while True:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        print(1)
    else:
        numlist = range(n + 1, 2 * n + 1)
        print(sum(map(lambda x: all(x % j for j in range(2, x)), numlist)))
"""
