# 일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다. 그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다. 이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다. 이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.

# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.
# 예를 들어, 4개의 문서(A, B, C, D)가 순서대로 인쇄 대기목록에 있고 중요도가 2 1 3 2 라면 C D A B 순으로 인쇄하게 됩니다.

# 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 알고 싶습니다. 위의 예에서 C는 1번째로, A는 3번째로 인쇄됩니다.

# 현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.
# 인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.
# location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.



# ------------- loop --------------
# 
# for i,v in enumerate(arr)
#   q.append((v,i)) # value,index 
#   반드시 뒤에 value와 index가 바뀌어 들어갔음을 주석으로 남기자
# 
# ----------------------------------------


from collections import deque
def solution(prior,loc):
    # q = []
    # for i,v in enumerate(prior):
    #     q.append((v,i))
    
    # d = deque(q)
    # y = True
    # while y:
    #     left = d.popleft()
    #     for v,idx in d:
    #         if left[0] < v :
    #             d.append(left)
    #             break
            
    #     if len(d) < len(q):
    #         y = False
    #         d.appendleft(left)
    #         print(d)
    #         for j in range(len(d)):
    #             if d[j][1] == loc:
    #                 return j+1 

# ----------------------------

    # q = []
    # for i,v in enumerate(prior):
    #     q.append((v,i))
    
    # # 같은숫자가 있는 경우에 어떻게 처리할것인가? 아래 소팅으로는 해결이 안된다.
    # q = [(x,v) for x,v in sorted(q, key=lambda x:x[0], reverse=True)]
    # d = deque(q)
    # print(d)

    # idx = 0
    # while d:
    #     idx += 1
    #     left = d.popleft()
    #     if left[1] == loc:
    #         return idx     

# -----------------------------
# 정답! 
    
    q = []
    for i,v in enumerate(prior):
        q.append((v,i))
    
    d = deque(q)
    return_idx = 0
    last_len = len(d)
    while d:
        left = d.popleft()
        for v,idx in d:
            if left[0] < v :
                d.append(left)
                break
        # 앞에서 뺀것이 이전 전체길이와 맞지 않을경우(맨앞이 나머지길이중에 가장긴 경우)
        # 맨앞에서 뺀것이 뒤에 나올것보다 작다면, 위에 if문을 타고 맨뒤로 다시 append 됐을꺼다 
        if len(d) != last_len:
            return_idx += 1 
            if left[1] == loc:
                return return_idx
        last_len = len(d)


# --------------------------------
# [x for x,v in sorted( s_num.items(), key=lambda x:x[1], reverse=True )]
# print(list(map(lambda x:x[0], q)))
# q = [x for x in sorted(q, key=lambda x:x[0], reverse=True)]
    



# prior = [2,1,3,2]
# loc = 2

# prior = [1, 1, 9, 1, 1, 1]
# loc = 0

prior = [1,2,8,3,4]
loc = 4

print(solution(prior,loc))





