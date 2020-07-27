"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-27
Baekjoon Online Judge Study - 3009(fourth point)
"""

xs = []
ys = []
for _ in range(3):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

print([a for a in xs if xs.count(a) == 1][0], [b for b in ys if ys.count(b) == 1][0])
