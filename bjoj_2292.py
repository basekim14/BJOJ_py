"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-12
Baekjoon Online Judge Study - 2292(honeycomb)
"""

N = int(input())

count = 1
mod = 6
rooms = 1
while N > count:
    rooms += 1
    count += mod
    mod += 6

print(rooms)
