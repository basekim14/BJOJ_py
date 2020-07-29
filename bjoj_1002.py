"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-30
Baekjoon Online Judge Study - 1002(taxi cab geometry)
"""

def count_targets():
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5
    l = sorted([d, r1, r2])
    if d == 0 and r1 == r2:
        return -1
    elif l[2] == l[0] + l[1]:
        return 1
    elif l[2] > l[0] + l[1]:
        return 0
    else:
        return 2

for _ in range(int(input())):
    print(count_targets())
