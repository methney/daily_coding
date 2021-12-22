

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    
class Solution:

    # 1 > 2 > 4 (2와 아래 1 비교, 2 > 1 이므로 l1 <=> l2 swap!) 
    # 1 > 3 > 4 
    # -------------------
    # 1 > 1 > 3 > 4  (바뀐뒷부분은 따라간다)
    # 2 > 4 (다시 위의 3과 2 비교, 3 > 2 이므로 l1 <=> l2 swap!)
    # -------------------
    # 1 > 1 > 2 > 4
    # 3 > 4 (다시 위의 4와 3 비교, 4 > 3 이므로 l2 <=> l2 swap!)
    # -------------------
    # 1 > 1 > 2 > 3 > 4
    # 4 (위의 4와 아래 4 비교, 4 = 4 이므로 no swap!, 하지만 l1이 더이상존재안함)
    # -------------------
    # 1 > 1 > 2 > 3 > 4 > 4
    # 
    def mergeTwoLists(self, l1:ListNode, l2:ListNode)->ListNode:
        if not l1 or (l2 and l1.val > l2.val) :
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
# aa.getListNode(bb)

