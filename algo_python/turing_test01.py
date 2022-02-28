
from collections import deque

import collections
def solution(arr:list):
    # arr = collections.deque(ops)
    newArr = []    
    retArr = []
    # 현재를 돌면서, 이전 2개를 확인해야하니깐..-2까지 봐야겠다.
    for i in range(len(arr)):
        start = i-2 if i-2 >= 0 else 0
        # print('i:', arr[i], arr[:i-1], arr[start:i])
        sArr = []
        if arr[i] not in ['C','D','+']:
            # 숫자라서 배열에 넣음 
            newArr.append(int(arr[i]))

        # C이면 바로 앞에꺼 배열에서 빼고
        if arr[i] == 'C' :
            newArr.pop()

        # D이면 2배곱 
        elif arr[i] == 'D':
            re = int(newArr[-1]) * 2
            newArr.append(re)

        # +이면 앞에 두개 더해
        elif arr[i] == '+' and len(newArr) > 2:
            a = newArr[-1]
            b = newArr[-2]
            newArr.append(int(a)+int(b))

    print(sum(newArr))

arr = ["5","2","C","D","+"] # 30
arr = ["5","-2","4","C","D","9","+","+"]
solution(arr)




