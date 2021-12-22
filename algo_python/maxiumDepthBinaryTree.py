
import collections
import copy

# tt = [3,9,20,null,null,15,7]
# 이게 책이나 지문에서 보면, TreeNode의 값을 위처럼 배열처럼 표기를 해놓는데..
# 그렇게 배열로 돌려서는 아래코드가 돌지 않는다. 
# 맨아래에 각각 tree.left = TreeNode(4) 이런식으로 값을 넣어주어야한다. 

# deque핵심은
# 뺄때는 popleft로 빼고
# 다시 넣을때는 그냥 append로 붙인다.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root:TreeNode): 
    if root is None:
        return 0

    # root를 이용해서 deque를 만들지만, 그냥 루트가 있는(3) 큐 구조체를 하나 만든거 불과하다.
    # 빼고 넣고하는 것은 아래서..
    queue = collections.deque([root])
    depth = 0

    # queue2 = copy.deepcopy(queue)
    # for _ in queue:
    #     print(_.val, queue2.popleft().val)

    
    while queue:
        depth+=1
        # print('len',len(queue))
        for i in range(len(queue)):
            # root 하나만 나옴
            cur_root = queue.popleft()
            if cur_root.left:
                queue.append(cur_root.left)
                # 도대체 이걸왜하는거야? 어차피 root를 넣어서 queue를 만들때에 이미 다 있어야하는거 아니야? 
                # 아니야..하나씩 움직이면서, 거기서 다시 하위것들을 붙이고..또 popleft로 진행하고 또 하위것들을 붙여서 마지막까지 가는거야..
                # 결국 구하는게 최대깊이이거든... depth를 구하는거지..
            if cur_root.right:
                queue.append(cur_root.right)
                # 여기서 20,7이 붙어
            # 결국뭐냐, root로 deque를 이용해서 queue를 만들어냈을때, len(queue)를 찍어보면 그냥 1이 나온다. queue.val = 3인거지..
        printQueue(queue)

    return depth

def printQueue(que:list):
    for _ in que:
        print(_.val)

tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.left.left = TreeNode(None)
tree.left.right = TreeNode(None)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

maxDepth(tree)