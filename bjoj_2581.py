"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-20
Baekjoon Online Judge Study - 1978(is prime)

"""

T = input()
numlist = list(map(int, input().split()))
conut = sum(map(lambda x: all(x % j for j in range(2, x)) and x > 1, numlist))
 
print(conut)
