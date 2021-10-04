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

        #  TreeNode로 할경우, stack은 루트인 4, 하나만 세팅된다. 
        while stack:
            node = stack.popleft() #pop()과 popleft()로 DFS, BFS를 구현할수 있다.
            print('popleft', node if node is None else node.val)
            # 부모 노드 부터 하향식 스왑
            if node:
                # node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)

                node.left, node.right = node.right, node.left

        return root


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


