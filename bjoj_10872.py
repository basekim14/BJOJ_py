"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-19
Baekjoon Online Judge Study - 10872(factorial)
"""

def factorial(n, _cache={}):
    if n in _cache:
        return _cache[n]
    
    result = n * factorial(n-1) if n > 1 else 1
    _cache[n] = result
    return result

print(factorial(int(input())))
