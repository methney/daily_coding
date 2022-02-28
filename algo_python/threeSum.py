from typing import ContextManager, List


# -------- 배열조작 --------------
# 
# result.append([i, j]) 처럼 배열을 담을수도 있다.
# 
# ------------------------------



nums = [-1,0,1,2,-1,-4]

# bruteforce
def threeSumBrute(nums:List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    for i in range(len(nums)-2):
        if i > 0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1, len(nums)-1):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            for k in range(j+1, len(nums)):
                if k > j+1 and nums[k] == nums[k-1] :
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
    

    return result

# print(threeSumBrute(nums))




# two pointer로 풀기 
def threeSum(nums:List[int])->List[List[int]]:
    result = []
    nums.sort()

    for i in range(len(nums)-2):
        # 왜 연속된2개가 같으면 break하는걸까?
        # 합이0을 구하는거라면, 남은2개가 각각 -값을 가져서 완성될수도 있는거잖아? 
        # 정의가 혹시 중복된 숫자가 없는것인가? (제한까지왜구현을해?)
        if i>0 and nums[i] == nums[i-1]:
            continue

        # 양끝을 정하고, 양쪽에서 출발하여 비교
        left, right = i+1, len(nums)-1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0 :
                left += 1
            elif sum > 0 :
                right -= 1
            else :
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left+1]:
                    left += 1 # 이뤄질수없는 조건은 빨리 넘어가도록 처리
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    
    return result

print(threeSum(nums))



