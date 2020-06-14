# Baekjoon Online Judge Study - 15552
# Author : ㄱㄱㅊ
# Title : fast sum
# Date : 20-06-14

from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    print(sum(int(i) for i in stdin.readline().split()))
