"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-06-14
Baekjoon Online Judge Study - 10950(A+B - 3)
"""

from sys import stdin

T = int(stdin.readline())
# result_list = []
for _ in range(T):
    print(sum(int(i) for i in stdin.readline().split()))
    # A, B = map(int, stdin.readline().split())
    # print(A + B)
    # result_list.append(A + B)

# for result in result_list:
    # print(result)

""" 입력과 출력 형태를 고려해도
이와 같은 형태는 정답 처리
"""
