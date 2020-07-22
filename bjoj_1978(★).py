"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-22
Baekjoon Online Judge Study - 1978(is prime)

"""

M = int(input())
N = int(input())
prime_list = []

for num in range(2 if M == 1 else M, N+1):
    if (lambda i: all(i % j for j in range(2, i)))(num):
        prime_list.append(num)

print(str(sum(prime_list))+"\n"+str(prime_list[0]) if prime_list else -1)


"""앞으로 자주 쓰게 될 소수 판별 람다식,
범위를 지정할 때 range를 쓸 경우 마지막 범위 + 1을 빼먹기 쉬
"""
