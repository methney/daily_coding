


# ------------- 조건문 --------------
# 
# if not len(stack) 을 만족하려면,
# stack이 비었다는 얘기겠지? 0 이면 False
# 
# ------------------------------

# 파이선알고리즘인터뷰 p182 
# 스택쌓기 
def solution(height):
    stack = []
    volume = 0

    # 포인트!
    # 1. 거리계산시에 블럭단위로 계산시에는 거리게산시 -1 해줌 
    # 2. distance(거리) X Water(한칸당물량,높이차)
    # 3. 현재 idx의 높이(height(idx))가 낮아지는 상황에서는 stack에 저장(담을수없다), height(idx)와 같거나 낮을때 담는다.
    # 4. while에서는 stack을 pop하지않고 stack[-1]등으로 비교하고 실제로 뺄때만 pop한다
    # 5. distance는 간단하게 idx와 마지막 스택요소간의 거리로 한다. 
    for i in range(len(height)):
        while stack and height[i]  > height[stack[-1]]:
            # print(i, '/', stack, height[i], '>', height[stack[-1]])
            top = stack.pop()
            if not len(stack):
                break
            # print('distance :', i , '-', stack[-1],'- 1 = ', i - stack[-1] - 1)
            # 거리계산하는데, stack에서 빼서쓴다고? 사실 stack이 지난 idx의 개념이자나 이상할게없다.
            # 마지막 -1은 이게 블럭하나가 기본적으로 1~2, 2~3씩 하나씩 통으로 잡아먹기 때문에..-1을 함으로 그부분을 상쇄.
            distance = i - stack[-1] - 1
            # 물을 담기 위해서 현재 idx가 3이라하면, 그 두개전인 idx:1와의 min값을 계산해서 최저기준에서부터 중간값(top:0)의 높이를 계산해서 1이란 물양을 계산
            waters = min(height[i], height[stack[-1]]) - height[top] 
            # print(distance,'*',waters, ' = ', distance * waters)
            # 그리고 최종적으로 거리 * 높이로 넓이를 계산함
            volume += distance * waters
        stack.append(i)
        print('------', stack)
    return volume
            

list = [0,1,0,2,1,0,1,3,2,1,2,1]
solution(list)

