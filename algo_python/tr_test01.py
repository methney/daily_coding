
import collections

# -------- 특정 문자에 의미를 부여하고 배열을 그대로 조작하는 문제 --------------
# 
# 문자열일때 문제가 될수 있으니, 연산이 들어갈때는 int() 화 해줄것!
# 맨뒤값을 pop하기전에 조건에 따라 확인할때는 newArr(-1) 로 확인할것!
# 
# ------------------------------------------------------------------


# 1. 좀 확인을 해보자면, 배열자체가 변경이 되면서 확장이 되는지.. 
#       , 마지막값만 수정하면 되는가? >> loop마지막에 이전값을 저장
#       , 이전값들을 이용하며 확장되나? >> 
#       , 최대값이 갱신되는 것인가? >> max() 사용하며갱신
# 2. 리턴배열을 준비해야하는지 확인하는게 중요.
def solution(arr:list):
    newArr = []    
    for i in range(len(arr)):
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
arr = ["5","-2","4","C","D","9","+","+"] # 27
solution(arr)




