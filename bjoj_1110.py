"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-16
Baekjoon Online Judge Study - 1110(sum cycle)
"""

N = int((input() + "0")[0:2])
res, count = N, 0
while True:
    a, b = divmod(res, 10)
    res = (b*10) + ((a+b) % 10)
    count +=1
    
    if res == N:
        print(count)
        break
