from bisect import bisect_left, bisect_right
from typing import List


def search(nums:List[int], target:int) -> int:

    left,right = 0, len(nums)-1
    while left <= right: # 같을때도?
        mid = (left + right)//2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else :
            return mid 
    return -1
    

nums = [0,1,2,3,4,5]
target = 4
print(search(nums,target))