"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-08-14
Baekjoon Online Judge Study - 11050(ring)
"""

from math import factorial

n, k = map(int, input().split())
bc = factorial(n) // (factorial(k) * factorial(n-k))
print(bc)
