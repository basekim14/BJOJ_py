"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-13
Baekjoon Online Judge Study - 1193(find fraction)
"""

"""
def find_fraction(X):
    if X == 1:
        return "1/1"
    
    RC = 1 # ROW & COL
    matrix = []
    while X > RC * (RC+1) // 2:
        RC += 1

    for row in range(1, RC+1):
        tmp = []
        for col in range(1, RC+1):
            tmp.append(str(row)+"/"+str(col))
        matrix.append(tmp)

    filtered = (0, RC, 1) if RC % 2 == 1 else (RC-1, -1, -1)
    result = [matrix[RC-1-i][i] for i in range(*filtered)]
    idx = X-1 - ((RC - 1) * RC // 2)
    return result[idx]
"""
def find_fraction(X):
    if X == 1:
        return "1/1"
    
    LINES = 1
    while X > LINES * (LINES+1) // 2:
        LINES += 1

    num = X - ((LINES - 1) * LINES // 2)

    if LINES % 2 == 1:
        return str(LINES+1-num)+"/"+str(num)
    else:
        return str(num)+"/"+str(LINES+1-num)
    
X = int(input())
print(find_fraction(X))

