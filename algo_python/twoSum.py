
from typing import Collection, List


nums = [1,2,3,4]
target = 5
ret = []

# 리스트에서 합이 5를 만드는 배열의 인덱스를 찾는문제 
# 전제가 중복된게 있어서느 안돼..
# 첫번째 항목으로 5-i인것을 complement로 한다라고 정의
# nums의 i+1:에서 complement가 있다면, i의 index와 complement의 index값을 찾겠다. (근데, i+1을 최종적으로 더하는건? 왜?)
# 5-1 = 4이고 4가 [2,3,4]중에있다면, 새로운배열에 1의인덱스인 0과, 5를만드는 값(4)의 index가 2가 되는데..시작이 i+1이니(첫번쨰것을 제하고..)..그걸다시 보상해줌(원래의 배열에서의 index값을 구함)
# 하나더 확인할것! ret.append(1,2)을 넣은게 아니라 배열 ret.append([1,2]) 을 넣은거다. 오해없도록!
def twoSum(nums:List[int], target:int) -> List[int]:
    for i,n in enumerate(nums):
        complement = target - n

        if complement in nums[i+1:]:
            ret.append([nums.index(n), nums[i+1:].index(complement) + (i+1)])

twoSum(nums,target)
print(ret)

# 문제가 인덱스를 구하는 것이라 Two Pointer는 사용할수가 없다. 
# 만약 합을 이루는 값에 대한 것이라면 Two pointer로...
