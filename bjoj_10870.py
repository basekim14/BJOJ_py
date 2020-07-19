"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-19
Baekjoon Online Judge Study - 10870(fibonacci)
"""

def fibo(n, _cache={}):
    if n in _cache:
        return _cache[n]
    
    result = fibo(n-1) + fibo(n-2) if n > 1 else n
    _cache[n] = result
    return result

print(fibo(int(input())))
