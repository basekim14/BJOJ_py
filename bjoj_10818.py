"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-20
Baekjoon Online Judge Study - 10818(min&max)
"""

from sys import stdin

N = int(stdin.readline())
mylist = list(map(int, stdin.readline().split()))
print(min(mylist), max(mylist))

"""
# 첫째줄, 둘째줄 입력 고려 x
_,*v=map(int,stdin.read().split())
print(min(v),max(v))
"""
