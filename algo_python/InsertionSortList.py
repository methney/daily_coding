

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    
    def insertionSortList(self, head:ListNode) -> ListNode:
        cur = parent = ListNode(None)

        if cur.next.val < head.val:
            print('valid')
    
aa = Solution()
aa.insertionSortList(ListNode(4))