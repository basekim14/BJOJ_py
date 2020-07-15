"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-16
Baekjoon Online Judge Study - 10250(ACM hotel)
"""

from sys import stdin

for _ in range(int(stdin.readline())):
    H, W, N = map(int, stdin.readline().split())
    print((H if N % H == 0 else N % H)*100 + (N // H if N % H == 0 else N // H + 1))
