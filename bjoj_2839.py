"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-11
Baekjoon Online Judge Study - 2839(deliver sugar)
"""

from sys import stdin

N = int(stdin.readline())
numslist = []

for i in range(N//3+1):
    for j in range(N//5+1):
      if 3*i + 5*j == N:
          numslist.append((i, j))

if numslist:
    print(min([sum(nums) for nums in numslist]))
else:
    print(-1)
