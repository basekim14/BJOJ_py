"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-28
Baekjoon Online Judge Study - 4153(right-angled triangle)
"""

while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        print("right")
    else:
        print("wrong")

    
    
