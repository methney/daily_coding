# 이렇게 A → C → B의 순서로 처리하면 각 작업의 요청부터 종료까지 걸린 시간의 평균은 9ms(= (3 + 7 + 17) / 3)가 됩니다.

# 각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)
# 입출력 예
# jobs	return
# [[0, 3], [1, 9], [2, 6]]	9
# 입출력 예 설명
# 문제에 주어진 예와 같습니다.

# 0ms 시점에 3ms 걸리는 작업 요청이 들어옵니다.
# 1ms 시점에 9ms 걸리는 작업 요청이 들어옵니다.
# 2ms 시점에 6ms 걸리는 작업 요청이 들어옵니다.

import heapq
def solution(jobs):
    # lenJ = len(jobs)
    # arr, answer = [],[]
    # jobs.sort()
    # heapq.heappush(arr,(jobs[0][1],0))
    # while arr:
    #     d = heapq.heappop(arr)
    #     jobs.pop(0)
    #     idx = 0
    #     last = 0
    #     print(last,'<', lenJ-1)
        # while last < d[0] + jobs[idx][1]:
        #     heapq.heappush(arr,(d[0] + jobs[idx][1],d[1]))
        #     last = d[0] + jobs[idx][1]
        #     if idx < lenJ-1 :
        #         idx += 1
        #     print(idx)
        # answer.append(d[1] - d[0])
        # print('------------')

# --------------------------------------------------
    # lenJ = len(jobs)
    # jobs.sort()
    # arr,answer = [],[]
    # heapq.heappush(arr,(jobs[0][1],0))
    # jobs.pop(0)

    # while arr:
    #     d = heapq.heappop(arr)
    #     answer.append(d[0])
    #     last = d[0]
    #     while jobs:
    #         job = jobs.pop(0)
    #         print(last,'+',job[1])
    #         heapq.heappush(arr, (last + job[1], job[0]))
    #         last = job[1]
    #         break
    # # print(answer)
    # hap = 0
    # for a in answer:
    #     hap += a

    # print(hap//lenJ)
# -------------------------------------------- 

    # lenJ = len(jobs)
    # jobs.sort()
    # arr,answer = [],[]
    # j = jobs.pop(0)
    # heapq.heappush(arr, (j[1]-j[0], j[0], j[1])) # 
    # cur, tmp = 0, 0
    # while arr :
    #     d = heapq.heappop(arr) 
    #     if d[1] < cur: #겹쳐있어서 우선적으로 처리하고 나머지 것들은 뒤로 밀릴때
    #         tmp = cur + d[2] - d[1]
    #     else : # 이상일때(같을때포함)
    #         tmp = d[2]
    #     answer.append(tmp)
    #     cur += d[2]
    #     while jobs:
    #         job = jobs.pop(0) # job[0]: 시작위치, job[1]: 걸린시간
    #         # It will be wrong when put the data into heapq
    #         # because it will be organized after putting this like that(part of 'cur') ->> heapq.heappush(arr, (job[1], job[0], job[1] + cur)) 
    #         # 두번째 while문인 여기서 cur를 사용하기가 애매한거지.. 첫번재 idx1안에서 두번째while문의 idx2라는건.. 첫번째의 cur값을 계속 사용해야하는거라..
    #         # 연속된 누적값을 사용하고 싶을때는 어려움이 있다.

            
    #         # 
    #         heapq.heappush(arr, (job[1], job[0]))
    # print(answer)
    # return int(sum(answer)//lenJ)


# -------------------------------------
    # 우선순위사용안함
    # 총3개일때, 첫번째를 제외한 2개가 모두 첫번째 작업이 끝나기전에 시작하는 케이스에서
    # 우선순위를 정해야 하는 케이스를 처리애야함, 우선순위큐없이 우선순위를 정해야 하는 것이라 어려움이 있음 

    # from collections import deque
    # lenJ = len(jobs)
    # jobs.sort()
    # arr,answer = deque(),[]
    # j = jobs.pop(0)
    # arr.append((j[0],j[1]))
    # cur, tmp = 0,0
    # while arr:
    #     d = arr.popleft()
    #     print(d, cur)
    #     if d[0] < cur :
    #         tmp = cur + d[1] - d[0]
    #     else : 
    #         tmp = d[1]
    #     answer.append(tmp)
    #     while jobs:
    #         job = jobs.pop(0)
    #         if job[0] < cur:
    #             arr.appendleft((job[0],job[1]))
    #         else :
    #             arr.append((job[0],job[1]))
    #     cur += d[1]
    # print(answer)

# ----------------------------------------------------

    # 근데 데이터를 큐에 넣을때에 첫번째 태스크가 끝나기전에 시작하는 케이스와 일반 케이스를 어떻게 구분하느냐는거지 > 나올때가능한가?(pop할때)
    # 이거 이중배열 우선순위큐로 해보자! (같은 위치에서 시작했을때를 대비해서도 좋은방법이다.)
    # [시작위치][걸린시간] 이렇게하면, 만약 두 경우가 다 첫번째태스크 종료 이전에 위치한다고 했을때, 
    # 어떤것을 먼저처리할까? 당근 시작위치가 앞서는거잖아? 근데..이렇게하면, 첫번째 테스트케이스에서 이미 나가리다([ [0, 3], [1,9], [2,6] ]) > (2,6)이게 앞서야한다.
    # 결국 보면, [0,3] 이후에 [1, 9+3] 이냐, [2, 6+3] 이냐(3이 이전 태스크종료시점) 이 차이(12-1 또는 9-2)거든..범위안에 들때는...
    # 이전에 내가했던것과의 차이는 두번째 loop문는 매번 남은 배열에서 반복해서 시작위치와 끝위치를 만들고 그 차이만큼을 우선순위의 value로 두는거지 
    # 범위밖일때는 그냥 뒷값을 더하는 과정없이 그냥 하면되고...    

    lenJ = len(jobs)
    jobs.sort()
    arr,answer = [],[]
    cur, tmp = 0, 0
    j = jobs.pop(0)
    heapq.heappush(arr, (cur+j[1]-j[0], j[0], j[1])) 

    cur = j[1]
    while arr :
        # 하나 빼서 적용하고 아래의 while안에서 다시 다음 후보를 채워넣는다.
        # 그럼 이전에 아래 whle안에서 후보군으로 여러개의 값이 arr에 채워졌을텐데.. 그걸 다시 비워야하는거아닌가? 
        # answer에 최종값을 넣고나서 arr를 비우고 다시 시작해야겠네...
        d = heapq.heappop(arr) 
        answer.append(d[0])
        # -> 여기서 arr이 싹다 비우는걸 하나 만들어라!
        arr = []
        while True:
            if len(jobs) == 0 :
                break
            job = jobs.pop(0)
            print(cur,'>',job[0])
            if cur > job[0]:
                heapq.heappush(arr, (cur+job[1]-job[0], job[0], job[1]))
                print(arr)
                continue
            else : 
                # 이전테스크에 상관없이 실행이 가능한 것들은 그냥 등록한다? 
                # 이번엔 그렇지만, 다른테스크에서 걸릴수도 있잖아? 
                jobs.append(job)
                break # jobs가 sort가 되있기에 가능하다.

        cur += j[1]
    return sum(answer)//lenJ

jobs = [[0, 3], [2,6], [1, 9]]	
# jobs = [[0, 5], [2, 10], [10000, 2]] # 6
# jobs = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]  # 72
print(solution(jobs))