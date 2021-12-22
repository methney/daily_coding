
from typing import Collection, List

# 이게 toptal 시험문제로 나왔던, 미로풀기인데...
# 이거 BFS queue로 풀어야한다(사실큐라고 하지만 그냥 string에 담아서푼다)
# shortestPath.py 참고할것 


class A :

    store = {}
    turn = { '0':'1/0', '1':'0/1', '2':'-1/0', '3':'0/-1'}
    sum = 0
    xIdx,yIdx = 0,0

    def solution(self,A):
        # self.move(A, 0, 0,self.turn.get('0'))
        self.move(A, self.turn.get('0'))
        return self.sum

    # def move(self, arr, xIdx, yIdx, turn):
    #     print(str(xIdx)+','+str(yIdx)+','+turn)
    #     tIdx = 0
    #     xDiff = turn.split('/')[0]
    #     yDiff = turn.split('/')[1]
    #     st = ''.join([str(xIdx),str(yIdx)])
    #     while arr[yIdx]:
    #         sTrack = list(arr[yIdx])
    #         if self.store.get(st):
    #             return
    #         while sTrack[xIdx] and not self.store.get(st):
    #             if sTrack[xIdx]=='X':
    #                 tIdx+=1
    #                 return self.move(arr,xIdx,yIdx,self.turn.get(str(tIdx%4)))
    #             self.sum += 1
    #             xIdx+=int(xDiff)
    #             self.store[''.join([str(xIdx),str(yIdx)])] = True
    #         yIdx+=int(yDiff)
    #         self.sum+=1


    def move(self, A, turn):
        tIdx = 0
        xDiff = turn.split('/')[0]
        yDiff = turn.split('/')[1]
        while A[self.xIdx] and A[self.yIdx]:
            self.xIdx+=xDiff
            self.yIdx+=yDiff
            if 






arr = ['...X..','....XX.','..XX..']
aa = A()
print(aa.solution(arr))

        