class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    
    def reverseList(self, node: ListNode, prev:ListNode=None) -> ListNode:
        # print(node.val)
        if not node:
            return prev
        next, node.next = node.next, prev
        # print(next.val if next else 'None') 
        # print(node.val if node else 'None') 
        return self.reverseList(next,node)

    def getListNode(self, l:ListNode):
        if l:
            print(l.val)
        if l.next:
            self.getListNode(l.next)


l1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))

aa = Solution()
bb = aa.reverseList(l1)
aa.getListNode(bb)