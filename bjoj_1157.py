"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-02
Baekjoon Online Judge Study - 1157(word study)
"""

from sys import stdin

word = stdin.readline().strip().lower()
count = {}

for token in word:
    if token not in count:
        count.setdefault(token, 1)
    else:
        count[token] += 1

max_count = max(count.values())
result = ""

for key, value in count.items():
    if value == max_count:
        result += key

print(result.upper() if len(result)==1 else "?")
