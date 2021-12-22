from bisect import bisect_left, bisect_right
from typing import List


def search(nums:List[int], target:int) -> int:
    # index = bisect_left(nums,target) # 값의 왼쪽 idx = 값자체의 index
    # index = bisect_right(nums,target) # 값이 가장 오른쪽 idx = 값 오른쪽의 index
    if index < len(nums) and nums[index] == target:
        return index
    else :
        return -1
    return index

nums = [0,1,2,3,4,5]
target = 3
print(search(nums,target))