"""
ㄱㄱㅊ <basekim14@gmail.com>, 21-02-06
Baekjoon Online Judge Study - 11757(big-integer)
"""

from sys import stdin

# A, B = map(int, stdin.readline().split())
# print(A+B)

A = 123456789123456789123456789
B = 987654321987654321987654321



res1 = A % (10 ** 9)
res2 = A // (10 ** 9)
print(res1, res2)

"""
max_len = len(A) if len(A) >= len(B) else len(B)

print(max_len // 9)
print(A[-9:-1])
for i in range(-1, -1 * (max_len // 9), -1):
    print(A[9*i-1:9*(i-1)-1])
"""
# splited_A = list(map(lambda x: x+2, range(5)))

# print(splited_A)
