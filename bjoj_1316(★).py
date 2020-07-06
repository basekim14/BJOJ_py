"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-07-06
Baekjoon Online Judge Study - 1316(group words)
"""

count = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key = word.find):
        count += 1    
print(count)
