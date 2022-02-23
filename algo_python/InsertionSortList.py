

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    
    def insertionSortList(self, head:ListNode) -> ListNode:
        cur = parent = ListNode(None)
        i = 0
        while head:
            # print(i,cur.next)
            i+=1
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            cur.next, head.next, head = head, cur.next, head.next
            
            # 첫번째---------------------------------
            # cur.next = head 하면, None -> 4가 붙는다고 생각하겠지만, 사실은 None->4 뒤로 2->1->3 다 따라붙는다. (이게핵심) head는 비어있게되나?
            # 일단 두번째 while안에서 cur = cur.next 실행(만족하면)
            # head.next = cur.next를 하면, 4-2-1-3(cur.next) 이거를 head.next (4뒤에)
            # 그럼 cur에 None-4, head에는 4-2-1-3
            # 그리고 다시 head = head.next를 통해서 2-1-3이 된다. 
            # 결국 첫번째 사이클이 끝나고 None-4(cur), 2-1-3(head) 가 된다.
            
            # 두번째 -----------------------------------
            # 4 < 2 이어서 두번째 while비실행
            # cur.next = head, None-(2-1-3)-4 (cur)
            # head.next = cur.next, (2-1-3)(cur.next)
            # cur(None-2-4), head(2-1-3)
            # head = head.next, head(1-3) 

            # 세번째 -----------------------------------
            # 2 < 1
            # cur.next = head, cur(None-(1-3)-2-4)
            # head.next = cur.next, (1-3)(cur.next)
            # cur(None-1-2-4), head(1-3)
            # head = head.next, head(3)

            # 네번째 -----------------------------------
            # 1 < 3 , 두번째 while실행, cur = cur.next, cur(1-2-4), haed(3)
            # 2 < 3 , 두번째 while재실행, cur = cur.next, cur(2-4), head(3)
            # cur.next = head, cur(2-(3)-4)
            # head.next = cur.next, 3 (cur.next)
            # cur(2-3-4), head(3)
            # head = head.next (이건 없고..)

            # cur를 다시 맨처음 None으로 초기화
            cur = parent

        # print(self.getList(cur.next))
        return cur.next
    
    def getList(self,l:ListNode):
        if l:
            print(l.val)
        if l.next :
            self.getList(l.next)


aa = Solution()
bb = aa.insertionSortList(ListNode(4,ListNode(2,ListNode(1,ListNode(3)))))
aa.getList(bb)