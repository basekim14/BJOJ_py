"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-31
Baekjoon Online Judge Study - 5086(multiple and factor)
"""

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    elif a % b == 0:
        print("multiple")
    elif b % a == 0:
        print("factor")
    else:
        print("neither")
