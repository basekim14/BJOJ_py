"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-20
Baekjoon Online Judge Study - 1978(is prime)

"""

T = input()
numlist = list(map(int, input().split()))
conut = 0
 
for i in numlist:
    if i == 1 :
        continue
    if len([1 for z in [j for j in range(2, i)] if i % z == 0]) == 0:
        conut+=1
 
print(conut)
