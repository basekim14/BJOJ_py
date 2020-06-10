# Baekjoon Online Judge Study - 1003
# Author : ㄱㄱㅊ
# Title : fibonacci
# Date : 20-06-10

class Fibocount:
    fibocount = [[0, 0]] * 41
    
    def __init__(self):
        self.zerocount = 0
        self.onecount = 0

    def __del__(self):
        pass

    def fibonacci(self, n):
        # self.fibocount[n] = [0, 0]
        if (n == 0):
            self.fibocount[n][0] += 1
            return 0
        elif (n == 1):
            self.fibocount[n][1] += 1
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)
            # return (self.fibocount[n-1] if self.fibocount[n-1] else self.fibonacci(n-1)) + (self.fibocount[n-2] if self.fibocount[n-2] else self.fibonacci(n-2))

"""
printlist = []
for i in range(0, 41):
    F = Fibocount()
    F.fibonacci(i)
    printlist.append((F.zerocount, F.onecount))
print(printlist)
"""

"""

T = int(input())
Nlist = []
for i in range(T):
    Nlist.append(int(input()))


for N in Nlist:
    F = Fibocount()
    F.fibonacci(N)
    print(F.fibocount[N][0], F.fibocount[N][1])

"""

fibocount = [[0, 0]] * 41
fibocount[0] = [1, 0]
fibocount[1] = [0, 1]

def get_fibocount(n):
    if sum(fibocount[n]):
        return fibocount[n]
    
    else:
        a = (fibocount[n-1] if fibocount[n-1] else get_fibocount(n-1)).copy()
        print(a)
        b = (fibocount[n-2] if fibocount[n-2] else get_fibocount(n-2)).copy()
        print(b)
        fibocount[n] = [x+y for x, y in zip(a, b)]
        
            
        return fibocount[n]
        
        """
        fibocount[n] = (fibocount[n-1] if fibocount[n-1] else fibonacci(n-1))\
                       + (fibocount[n-2] if fibocount[n-2] else fibonacci(n-2))
        """

print(get_fibocount(3))

