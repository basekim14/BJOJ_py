"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-30
Baekjoon Online Judge Study - 10809(find alphabet)
"""

from sys import stdin

S = stdin.readline()
alphabet = [chr(v) for v in range(97, 123)]
for token in alphabet:
    print(S.find(token), end=" ")
