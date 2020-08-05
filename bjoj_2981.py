"""
ㄱㄱㅊ <basekim14@gmail.com>, 20-08-05
Baekjoon Online Judge Study - 2981(checkpoint)
"""

nums = []
res = []
for _ in range(int(input())):
    nums.append(int(input()))

for i in range(2, nums[1]-nums[0]+1):
    if not any([y % i for y in [x - nums[0] for x in nums[1:]]]):
        res.append(str(i))
    # for num in [num - nums[0] for num in nums[1:]]:
        
print(" ".join(res))        
