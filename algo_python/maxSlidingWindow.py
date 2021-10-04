
nums = [1,3,-1,-3,5,3,6,7]
k=3
r=[]

for i in range(len(nums)-k+1):
  r.append(max(nums[i:i+k]))


# print(r)

# 마지막3에 해당하는 -3은 출력되지 않는다
print(nums[0:3])

  