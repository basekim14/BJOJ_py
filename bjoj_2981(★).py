"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-08-05
Baekjoon Online Judge Study - 2981(checkpoint)
"""

def gcd(a, b):
    r = a % b
    while r > 0:
        a = b
        b = r
        r = a % b
    return b

def div_list(n):
    divs = [n]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if n//i != i:
                divs.append(n//i) 
    divs.sort()
    return divs 

nums1 = []
nums2 = []
res = []
for _ in range(int(input())):
    nums1.append(int(input()))

for i in range(len(nums1)-1):
    nums2.append(nums1[i+1]-nums1[i])

nums2.sort()

g = nums2[0]
if len(nums2) != 1:
    for num in nums2[1:]:
        g = gcd(g, num)

for i in div_list(g):
    print(i, end=" ")

