

class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SList(object):
    def __init__(self):
        self.head = Node(None)
        self.size = 0

    def selectNode(self, idx):
        if idx >= self.size:
            print("Index Error")
            return None
        if idx == 0:
            return self.head
        else:
            # target을 사용하는 이유는 무엇인가?
            # 배열을 사용해야하는 경우에 하나의 index값으로 바로 지정할 수 없으므로
            # 순서대로 이후로, 이전으로 연결하기 위해서 사용한다.
            target = self.head
            for cnt in range(idx):
                target = target.next
            return target

    def is_empty(self):
        if self.size != 0:
            return False
        else:
            return True

    def appendleft(self, value):
        # 없으면, 앞에 하나 추가하면되고
        # 있으면, 추가되는 Node의 next값을 self.head(현재)로 한다.
        if self.is_empty():
            self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        self.size += 1

    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.size += 1
        # 추가는 맨오른쪽에 할것인데..
        # 맨오른쪽은.. 배열에서나 표현이 가능한것이자나...그렇다면, target을 사용해야지..
        else:
            target = self.head
            while target.next != None:
                target = target.next
            # 위의 while이 끝나고 나면, 아마도 젤뒤에 와있겠지..
            target.next = Node(value)
            self.size += 1

    # 특정위치에 값을 넣는다.
    def insert(self, value, idx):
        # linkedlist가 비어있는 경우 그냥 처음에 넣는다.
        if self.is_empty():
            self.head = Node(value)
            self.size += 1
        # 비어있지 않으나 idx값이 그냥 0인경우,
        elif idx == 0:
            # 첫번째 Node에 새로운 Node를 넣고 next로 이전의 head를 지정한다.
            self.head = Node(value, self.head)
            self.size += 1
        # 비어있지도 않고, idx값도 0이 아닌 값으로 지정된 경우,
        # 해당 idx까지 이동해야하겠지? 배열이 아니므로, 순서대로 이동을 해야해 >> target을 사용해야지..
        else:
            # target = self.head 보통을 이렇게 시작하겠지만, idx값이 지정되어있으므로..이전 Node를 일단 구한다
            target = self.selectNode(idx - 1)

            # 기저, 이전값이 없다면, 그냥..아무것도 할수가 없다. linkedlist이기 때문에..
            if target == None:
                return

            # 값을 linkedlist 중간에 넣어야하는 경우,
            # tmp를 이용해서 사이를 벌린다.
            newNode = Node(value)
            tmp = target.next
            target.next = newNode
            newNode.next = tmp
            self.size += 1

    # 삭제, 비어있는 경우 return Error
    # idx 값이 size 보다 크다면..
    # Node삭제는 어떻게 해야하나... 일단, 해당노드를 지우고 이후와 이전을 잇는 작업
    def delete(self, idx):
        if self.is_empty():
            print("Error: Empty Linked List")
            return
        elif idx >= self.size :
            print('Overflow: index Error')
            return
        else :
            target = self.selectNode(idx-1)
            deltarget = target.next
            target.next = target.next.next
            del(deltarget)
            self.size -= 1


    # 현재목록을 프린트한다
    # head부터 출력을 하면 되겠지?
    def printlist(self):
        target = self.head
        # list가 있다면,
        while target:
            if target.next != None:
                print(target.data, ' > ', end=' ')
            else:
                print(target.data)
            target = target.next

    def listSize(self):
        return self.size

mylist = SList()
mylist.append('A')
mylist.printlist()
mylist.append('B')
mylist.printlist()
mylist.append('C')
mylist.printlist()
mylist.insert('D', 1)
mylist.printlist()
mylist.appendleft('E')
mylist.printlist()
print(mylist.listSize())
mylist.delete(0)
mylist.printlist()
print(mylist.listSize())
mylist.delete(3)
mylist.printlist()
mylist.delete(0)
mylist.printlist()
mylist.appendleft('A')
mylist.printlist()


# 돌린결과물 
# A
# A  >  B
# A  >  B  >  C
# A  >  D  >  B  >  C
# E  >  A  >  D  >  B  >  C
# 5
# E  >  D  >  B  >  C
# 4
# E  >  D  >  B
# E  >  B
# A  >  E  >  B
