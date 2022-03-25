#!/usr/bin/env python3


# -------------------------------------------
# BST
# O(log(n))
# 검색,게임,자동완성작업 및 그래픽에 사용
# -------------------------------------------


# 출력을 위한..
def printVal(obj):
    if obj is not None:
        print(type(obj))
    if obj.root is not None:
        _printVal(obj.root)

def _printVal(node):
    if node.data is not None:
        print(node.data)
    if node.left is not None:
        _printVal(node.left)
    if node.right is not None:
        _printVal(node.right)


class Node(object):
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    # 현재값과 현재의 노드하고 비교해서
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        aa = self.root is not None
        # print('aa', aa)
        return aa

    # node가 비었다면, 들어온 값을 그냥 Node에 넣는다.
    # 값이 있다면, 작으면 left, 크면 right로 삽입
    def _insert_value(self, node, data):
        # print('node is none' if node is None else 'node is not none')
        if node is None:
            node = Node(data)
            # print('node', node.data)
        else:
            # 같은 값을 들어올수 없겠지? 아니 같은값이 들어오지 않는다고 전제를 해버려야..
            # print(data, '<', node.data, 'then left')
            if data < node.data:
                # recursive하게 처리하는데..
                # root부터 시작해서 아래로 내려가는 형태..
                node.left = self._insert_value(node.left, data)
                # print('left', node.left.data)
            else:
                node.right = self._insert_value(node.right, data)
                # print('right', node.right.data)
        # print(node.data, data)
        return node

bst = BinarySearchTree()
bst.insert(3)
bst.insert(1)
bst.insert(5)
bst.insert(9)
bst.insert(2)
bst.insert(4)

    #     3
    # 1       5
    #     2       9
    #         4

printVal(bst)

    
