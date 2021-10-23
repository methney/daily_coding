

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    
class Solution:

    def mergeTwoLists(self, l1:ListNode, l2:ListNode)->ListNode:
        if not l1 or l2 and l1.val > l2.val :
            l1, l2 = l2, l1 
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

    def getListNode(self, l:ListNode):
        if l:
            print(l.val)
        if l.next:
            self.getListNode(l.next)


l1 = ListNode(1,ListNode(2,ListNode(4)))
l2 = ListNode(1,ListNode(3,ListNode(4)))

aa = Solution()
bb = aa.mergeTwoLists(l1,l2)
aa.getListNode(bb)
