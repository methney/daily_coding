

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
            # cur.next = head 하면, None -> 4가 붙는다고 생각하겠지만, 사실은 None->4 뒤로 2->1->3 다 따라붙는다. (이게핵심) head는 비어있게되나?
            # 일단 두번째 while안에서 cur = cur.next 실행(만족하면)
            # head.next = cur.next를 하면, 4-2-1-3(cur.next) 이거를 head.next (4뒤에)
            # 그럼 cur에 None-4, head에는 4-2-1-3
            # 그리고 다시 head = head.next를 통해서 2-1-3이 된다. 

            cur = parent

        return cur.next
    
    def getList(self,l:ListNode):
        if l:
            print(l.val)
        if l.next :
            self.getList(l.next)


aa = Solution()
bb = aa.insertionSortList(ListNode(4,ListNode(2,ListNode(1,ListNode(3)))))
aa.getList(bb)