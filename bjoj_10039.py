"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-17
Baekjoon Online Judge Study - 10039(average score)
"""

from sys import stdin

scores = []
for _ in range(5):
    scores.append(int(stdin.readline()))
print(sum(map(lambda x: x if x > 40 else 40, scores)) // len(scores))
