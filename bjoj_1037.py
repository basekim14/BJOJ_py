"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-08-02
Baekjoon Online Judge Study - 1037(proper divisor)
"""

nums = int(input())
divs = sorted(list(map(int, input().split())))
N = divs[0] * divs[-1]
# N = divs[nums//2] * divs[nums//2-1] if nums % 2 == 0 else divs[nums//2] ** 2
print(N)
