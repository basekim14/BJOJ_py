"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-05
Baekjoon Online Judge Study - 2941(croatia alphabet)
"""

croatia_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()

for alphabet in croatia_alphabet:
    if alphabet in word:
        word = word.replace(alphabet, "C")
print(len(word))
