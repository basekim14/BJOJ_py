"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-18
Baekjoon Online Judge Study - 1011(Fly me to the Alpha Centauri)
"""

def min_count(x, y):
    distance = y - x
    n = int(distance ** 0.5) # == math.trunc()
    if distance == n ** 2:
        return n*2 - 1
    elif distance <= n * (n + 1):
        return n*2
    else:
        return n*2 + 1

for _ in range(int(input())):           
    x, y = map(int, input().split())
    print(min_count(x, y))
    


"""수작업으로 규칙을 찾는 것이
때때로 더 나은 해답이 될 수 있다.
"""
