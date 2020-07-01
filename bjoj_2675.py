"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-02
Baekjoon Online Judge Study - 2675(string repetition)
"""

from sys import stdin

results = []
for _ in range(int(stdin.readline())):
    R, S = stdin.readline().split()
    results.append("".join([v * int(R) for v in S]))

for result in results:
    print(result)
