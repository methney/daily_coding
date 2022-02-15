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

    lenJ = len(jobs)
    jobs.sort()
    arr,answer = [],[]
    j = jobs.pop(0)
    heapq.heappush(arr,j + [j[1]])
    cur = j[1]
    while arr :
        d = heapq.heappop(arr)
        answer.append(d[1]-d[0])
        while jobs:
            job = jobs.pop(0)
            # if last > d[0]: # 3 > 0
            heapq.heappush(arr, job + [cur])
            cur = job[1]
        print(arr)

    # print(answer)

jobs = [[0, 3], [2,6], [1, 9]]	
solution(jobs)