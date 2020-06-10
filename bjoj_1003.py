# Baekjoon Online Judge Study - 1003
# Author : ㄱㄱㅊ
# Title : fibonacci
# Date : 20-06-10

class Fibocount:
    def __init__(self):
        self.zerocount = 0
        self.onecount = 0

    def fibonacci(self, n):
        if (n == 0):
            self.zerocount += 1
            return 0
        elif (n == 1):
            self.onecount += 1
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)

T = int(input())
Nlist = []
for i in range(T):
    Nlist.append(int(input()))

for N in Nlist:
    F = Fibocount()
    F.fibonacci(N)
    print(F.zerocount, F.onecount)
