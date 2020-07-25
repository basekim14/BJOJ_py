"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-26
Baekjoon Online Judge Study - 1085(escape from a rectangle)
"""

x, y, w, h = map(int, input().split())
print(min([x, y, w-x, h-y]))
