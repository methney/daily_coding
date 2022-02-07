

# 파이선알고리즘인터뷰 p182 
# 스택쌓기 
def solution(height):
    stack = []
    volume = 0

    for i in range(len(height)):
        while stack and height[i]  > height[stack[-1]]:
            print(i, '/', stack)
            top = stack.pop()
            if not len(stack):
                break
            print('distance :', i , '-', stack[-1],'- 1 = ', i - stack[-1] - 1)
            distance = i - stack[-1]-1
            waters = min(height[i], height[stack[-1]]) - height[top]
            print('waters min(', height[i],'/', height[stack[-1]], ') - ', height[top])
            # print(distance,'*',waters, ' = ', distance * waters)
            volume += distance * waters
        stack.append(i)
        print('------')
    return volume
            

list = [0,1,0,2,1,0,1,3,2,1,2,1]
solution(list)

