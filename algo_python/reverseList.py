class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, node: ListNode, prev:ListNode=None) -> ListNode:
        # print(self.getListNode(node))
        # print('-----------')
        if not node:
            return prev
        # 아마도 아래부분이 핵심인것 같은데, 이전에 sList 싱글러링크드리스트 풀때에 appendLeft할때에 Node(4,self.head)로 넣어줬는데..Node(value,next)인데, 의미가 뭐냐면 
        # 어떤값을 맨왼쪽(맨앞)에 넣고 이전값을 next에 self.head를 넣어처리하겠다는것. 하나씩 미루겠다의 의미..
        # 아래도 보면, next = node.next하고(전진), node.next = prev(후진,node의next를 이전과연결), reverseList(next,node)로처리 
        # 또 중요한것은 이렇게 해서 recursive하게 호출을 했다는 것! 
        next, node.next = node.next, prev
        # print(next.val if next else 'None', node.val if node else 'None') 
        return self.reverseList(next,node)

    def getListNode(self, l:ListNode):
        if l:
            print(l.val if l else 'None')
        if l and l.next:
            self.getListNode(l.next)


l1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))

aa = Solution()
bb = aa.reverseList(l1)
aa.getListNode(bb)
