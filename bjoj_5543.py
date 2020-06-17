"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-17
Baekjoon Online Judge Study - 5543(sanggeunnald)
"""

from sys import stdin

sangduk = int(stdin.readline())
joongduk = int(stdin.readline())
haduk = int(stdin.readline())
coke = int(stdin.readline())
sprite = int(stdin.readline())

burgers = [sangduk, joongduk, haduk]
drinks = [coke, sprite]
discount = 50

set_price = [burger_price + drink_price - discount\
             for burger_price in burgers\
             for drink_price in drinks]

print(min(set_price))
