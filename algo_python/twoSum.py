
from typing import Collection, List


nums = [1,2,3,4]
target = 5
ret = []


def twoSum(nums:List[int], target:int) -> List[int]:
    for i,n in enumerate(nums):
        complement = target - n

        if complement in nums[i+1:]:
            ret.append([nums.index(n), nums[i+1:].index(complement) + (i+1)])

twoSum(nums,target)
print(ret)

# 문제가 인덱스를 구하는 것이라 Two Pointer는 사용할수가 없다. 
# 만약 합을 이루는 값에 대한 것이라면 Two pointer로...

