
def solution(arr:list):
    
    brackets = {'}':'{', ']':'[', ')':'('}

    stack = []
    for bracket in arr :
        # brackets 이 열렸을때, stack에 넣고 
        if bracket in brackets.values() : 
            stack.append(bracket)
        # 여는게 아닐때는 (닫는괄호가 나오면) stack에서 마지막 뺀것과 arr의 현재값이 같을때만
        # stack에서 실제로 뺀다.
        else :
            print(brackets[bracket],'==', stack[-1], stack)
            if stack and brackets[bracket] == stack[-1]:
                stack.pop()
    if stack :
        return False
    return True
        

arr = ['{','(','[',']',')','}']
arr = ['{',']']
print(solution(arr))