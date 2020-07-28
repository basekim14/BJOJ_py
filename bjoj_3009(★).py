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

print(*[a for a in xs if xs.count(a) == 1], *[b for b in ys if ys.count(b) == 1])

"""요소가 하나인 리스트 -> 인덱스 x, 언팩
"""

"""3개의 값 입력 받음 -> 0 ^ a == a, a ^ a == 0인 성질을 이용,
3개의 값 중 무조건 두 값은 같은 값이므로 사용할 수 있는 방법
"""

"""
x = 0
for _ in range(3):
    x *= int(input()) # x 는 다른 두 요소와 상이한 고유한 요소로 정해
     
"""
