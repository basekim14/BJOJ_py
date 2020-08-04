"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-08-04
Baekjoon Online Judge Study - 2609(GCD & LCM)
"""

a, b = sorted(list(map(int, input().split())))

G, x = a, b
while x != 0:
    y = G % x
    G = x
    x = y

L = (a * b) // G

print(G)
print(L)

