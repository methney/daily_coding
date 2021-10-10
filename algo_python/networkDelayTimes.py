import collections
import heapq
from typing import List

# https://www.youtube.com/watch?v=KiCBXu4P-2Y
# 참고 

# 궁금한게 왜 처음에는 graph로 자료형을 관리하다가..
# dist부터는 큐로 하는거지? 
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # 그래프 자료형을 만든다. 
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            # print(u,v,w)
            graph[u].append((v, w))

        # print(graph)
        # {3: [(1, 5), (2, 2), (4, 1)], 2: [(1, 2)], 4: [(5, 1)], 5: [(6, 1)], 6: [(7, 1)], 7: [(8, 1)], 8: [(1, 1)]})

        # 큐 변수: [(소요 시간, 정점)]
        # 이렇게 생겼고 아래 heapq와 같이 사용(이건 외워라)
        Q = [(0, K)]

        # 딕셔너리 자료형을 만든다. 
        # what's for? 노드까지 걸리는 시간? 
        dist = collections.defaultdict(int)

        # 우선 순위 큐 최소값 기준으로 정점까지 최단 경로 삽입
        # 큐를 만들어서 위의 영상링크처럼 처리하게 된다.
        # 3 에서 연결가능한 노드를 찾아서 큐에 등록(3은 뺌)... 이걸 계속 반복..
        # 사실 while Q라는건 이 안에서 Q값이 변동이 있다는 것
        while Q:
            time, node = heapq.heappop(Q) # 이 heapq자체가 structure이다. 변수가 아니야 
            # print(time,node)

            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    # print(node, v,w)
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # 모든 노드 최단 경로 존재 여부 판별
        # 처음에 N값을 4로 했잖아.. 이 안에 못끝내면 -1을 리턴
        # 끝내면 끝내는데 걸린 시간을 리턴
        print(dist)
        if len(dist) == N:
            return max(dist.values())
        return -1


times = [[3,1,5],[3,2,2],[2,1,2],[3,4,1],[4,5,1],[5,6,1],[6,7,1],[7,8,1],[8,1,1]]
sol = Solution()
print(sol.networkDelayTime(times,8,3))