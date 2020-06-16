"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-16
Baekjoon Online Judge Study - 10871(number < x)
"""

from sys import stdin

N, X = map(int, stdin.readline().split())
# nlist = list(filter(lambda n: n < X, map(int, stdin.readline().split()[:N])))
nlist = [n for n in stdin.readline().split() if int(n) < X]
print(" ".join(nlist))
