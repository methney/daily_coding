

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    
    def insertionSortList(self, head:ListNode) -> ListNode:
        cur = parent = ListNode(None)
        i = 0
        while head:
            print(i,cur.next)
            i+=1
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            cur.next, head.next, head = head, cur.next, head.next
            # 다시맨앞으로 돌려서 확인 
            cur = parent

        return cur.next
    
    def getList(self,l:ListNode):
        if l:
            print(l.val)
        if l.next :
            self.getList(l.next)


aa = Solution()
bb = aa.insertionSortList(ListNode(4,ListNode(2,ListNode(1,ListNode(3)))))
# aa.getList(bb)