import collections
import heapq
from typing import List

# Breadth First Search grid shortest path
# https://www.youtube.com/watch?v=KiCBXu4P-2Y
# 참고 

# 궁금한게 왜 처음에는 graph로 자료형을 관리하다가..
# dist부터는 큐로 하는거지? 
# delayTime이라고..무슨지연시간이 아니라, 그냥 걸린시간이다.
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # 그래프 자료형을 만든다. 
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            # print(u,v,w)
            # v,w가 뭐야? (v:도착노드,w:시간)
            graph[u].append((v, w))

        # print(graph)
        # {3: [(1, 5), (2, 2), (4, 1)], 2: [(1, 2)], 4: [(5, 1)], 5: [(6, 1)], 6: [(7, 1)], 7: [(8, 1)], 8: [(1, 1)]})

        # 큐 변수: [(소요 시간, 정점)]
        # 이렇게 생겼고 아래 heapq와 같이 사용(이건 외워라)
        # 시간이 앞에있잖아? 시간순으로 뽑겠다는거다.
        Q = [(0, K)] #type은 그냥 list다..

        # 딕셔너리 자료형을 만든다(그냥 해시맵)
        # what's for? 노드까지 걸리는 시간? 
        # 재사용과 최종결과값을 저장하기 위한 용도
        dist = collections.defaultdict(int)

        # 우선 순위 큐 최소값 기준으로 정점까지 최단 경로 삽입
        # 큐를 만들어서 위의 영상링크처럼 처리하게 된다.
        # 3 에서 연결가능한 노드를 찾아서 큐에 등록(3은 뺌)... 이걸 계속 반복..
        # 사실 while Q라는건 이 안에서 Q값이 변동이 있다는 것
        while Q:
            # Q에서 최소값을 추출(그냥추출하면 최소값인거다, 자료구조가..)
            time, node = heapq.heappop(Q) # 이 heapq자체가 structure이다. 변수가 아니야
            # print(time,node)

            # 현재큐에서 최단시간인 time과 그 node
            # 그 node가 dist목록에 이미 있다면 큐에 등록하지 않음(시간이 가장 짧게 걸린것을 선택!)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    # print(node, v,w)
                    # 다음노드(v)까지 가기위한 시간(w) 
                    alt = time + w  
                    heapq.heappush(Q, (alt, v))
                    # 현재노드까지의 누적시간과 다음노드를 우선순위 큐에 다시 등록

        # 모든 노드 최단 경로 존재 여부 판별
        # 처음에 N값을 4로 했잖아.. 이 안에 못끝내면 -1을 리턴
        # 끝내면 끝내는데 걸린 시간을 리턴
        # print(dist)
        if len(dist) == N:
            return max(dist.values())
        return -1


times = [[3,1,5],[3,2,2],[2,1,2],[3,4,1],[4,5,1],[5,6,1],[6,7,1],[7,8,1],[8,1,1]]
sol = Solution()
print(sol.networkDelayTime(times,8,3))
# 3에서 출발해 모든노드가 신호를 받을수 있는 시간을 계산하라
# 8회만에 len(dist)가 8일때까지

# dist의 values가 뭐야? 
test = {1:2, 2:3, 3:4}
print(test.values())