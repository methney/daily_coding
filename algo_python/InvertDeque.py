import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])
        print(stack)
        #  TreeNode로 할경우, stack은 루트인 4, 하나만 세팅된다. 
        while stack:
            # print('--',len(stack))
            # 여기서 하나씩 pop하고..아래서 다시 stack에 자식노드를 append를 한다???
            node = stack.popleft() #pop(DFS)과 popleft(BFS)
            # print('popleft', 'NNN' if node is None else node.val)
            # 부모 노드 부터 하향식 스왑
            print('node:', node.val if node else 'None')
            if node:
                # invert를 어디서하느냐의 문제(1이냐2냐), DFS에서는 2번은 의미가 없네
                # 1.
                node.left, node.right = node.right, node.left

                # 왜 여기서 이걸 다시 stack에 다시 붙이나? 
                # 이런식으로 다시 넣게되면 순서가 완전 뒤로 밀리는거 아냐? 
                # 그냥 이렇게 해야 stack을 배열처럼 사용할수가 있다고 생각해라
                # print(stack)
                stack.append(node.left)
                stack.append(node.right)
                # print('stack:', stack)


                # 2.
                # node.left, node.right = node.right, node.left
        return root

    
# [4,2,7,1,3,6,9] 이렇게 표현을 하려나?
tree = TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(7)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(9)

sol = Solution()
sol.invertTree(tree)

# 선위
# pop 4 (4 하위의 2)
# pop 2 (2 하위는 1)
# pop 1 (1 하위는 없으므로 3)
# pop None (1하위 왼쪽)
# pop None (1하위 오른쪽)
# pop 3 (3 하위는 없으므로 다시 위로)
# pop None (3하위 왼쪽)
# pop None (3하위 오른쪽)
# pop 7 (7 하위의 6)
# pop 6 (6 하위는 없으므로 9)
# pop None (6하위 왼쪽)
# pop None (6하위 오른쪽)
# pop 9 (9 하위는 없으므로 끝)
# pop None (9하위 왼쪽)
# pop None (9하위 오른쪽)

# 선위 
# popleft 4
# popleft 7
# popleft 2
# popleft 9
# popleft 6
# popleft 3
# popleft 1
# popleft None (9하위 오른쪽)
# popleft None (9하위 왼쪽)
# popleft None (6하위 오른쪽)
# popleft None (6하위 왼쪽)
# popleft None (3하위 오른쪽)
# popleft None (3하위 왼쪽)
# popleft None (1하위 오른쪽)
# popleft None (1하위 왼쪽)

# 후위
# pop 4
# pop 7
# pop 9
# pop None
# pop None
# pop 6
# pop None
# pop None
# pop 2
# pop 3
# pop None
# pop None
# pop 1
# pop None
# pop None

# 후위
# popleft 4
# popleft 2
# popleft 7
# popleft 1
# popleft 3
# popleft 6
# popleft 9
# popleft None
# popleft None
# popleft None
# popleft None
# popleft None
# popleft None
# popleft None
# popleft None


