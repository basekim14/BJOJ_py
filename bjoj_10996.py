"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-18
Baekjoon Online Judge Study - 10996(print * - 21)
"""

from sys import stdin

def print_star(n):
    if n > 1:
        print(" ".join(["*"] * ((n+1) // 2)))
        print(" *" * (n//2))
        return
    else:
        print("*")
        return
    
N = int(stdin.readline())
for _ in range(N):
    print_star(N)
