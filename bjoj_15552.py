"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-14
Baekjoon Online Judge Study - 15552(fast sum)
"""

from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    print(sum(int(i) for i in stdin.readline().split()))
