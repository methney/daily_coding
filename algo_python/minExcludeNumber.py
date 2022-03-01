
from typing import Collection, List

# -------------- string 포함여부 ----------------------------
# 
#  
# 
# ---------------------------------------------------------

nums = [1,2,6,3]


def solution(A):
    re = []
    for a in range(max(A)):
        a = a + 1
        if a > 0 and not contain(a,A):
            re.append(a)
    return min(re)

def contain(a,A):
    if a in A:
        return A
    else :
        return None

print(solution(nums))
