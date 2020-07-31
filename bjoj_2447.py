"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-20
Baekjoon Online Judge Study - 2447(print start - 10)
"""

def print_star(N):
    if N == 3:
        return ["***", "* *", "***"]
    else:
        fir, sec, thi = print_star(N // 3)
        return [[fir*3, sec*3, thi*3], [fir+" "*N//3+fir, sec+" "*N//3+sec, ]

for floor in print_star(int(input())):
    print(floor)

    



