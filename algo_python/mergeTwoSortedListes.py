

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    
class Solution:

    # 신기하게 이거 지금 루프문이 아닌데...
    # sorting이 되고 있는거지.. 어떻게? 
    # 이게 바로 linkedlist의 특성을 잘 보여주는 것이다. (바뀐 뒷부분은 따라간다는 것!)

    # 1 > 2 > 4 (2와 아래 첫번째 1 비교, 2 > 1 이므로 l1 <=> l2 swap!) 
    # 1 > 3 > 4 
    # -------------------
    # l1.next = self.mergeTwoList(l1.next, l2)가 실행됨
    # ------------------- 
    # 1 > 1 > 3 > 4  (바뀐뒷부분은 따라간다)
    # 2 > 4 (다시 위의 3과 2 비교, 3 > 2 이므로 l1 <=> l2 swap!)
    # -------------------
    # l1.next = self.mergeTwoList(l1.next, l2)가 실행됨
    # ------------------- 
    # 1 > 1 > 2 > 4
    # 3 > 4 (다시 위의 4와 3 비교, 4 > 3 이므로 l2 <=> l2 swap!)
    # -------------------
    # l1.next = self.mergeTwoList(l1.next, l2)가 실행됨
    # ------------------- 
    # 1 > 1 > 2 > 3 > 4
    # 4 (위의 4와 아래 4 비교, 4 = 4 이므로 no swap!, 하지만 l1이 더이상존재안함)
    # -------------------
    # 1 > 1 > 2 > 3 > 4 > 4
    # 
    def mergeTwoLists(self, l1:ListNode, l2:ListNode)->ListNode:

        # not l1은 왜한거야? 
        # if not l1 or (l2 and l1.val > l2.val) :
        # 차라리 아래 조건이 맞는것 같아..
        if not (l1 and l2) or (l2 and l1.val > l2.val) :
            l1, l2 = l2, l1 
        # l1.next가 아니고? l1.next를 mergeTwoList에서 입력을 받게되는데..만약에 l1.next가 없으면 어쩌려고? 
        if l1:
            print(self.getListNode(l1.next))
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

