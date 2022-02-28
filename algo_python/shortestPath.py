import queue

# -------------------------------------------------------------
# 
# 미로찾기 문제!!!! (BFS로 미로찾는 아주 간단하고 좋은예)
# https://www.techwithtim.net/tutorials/breadth-first-search/
# 
# -------------------------------------------------------------

def createMaze():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", " ", " ","#"])
    maze.append(["#"," ", "#", "#", "#", " ","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#","#", "#", "#", "#", "X","#"])

    return maze

def createMaze2():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "X", "#"])

    return maze

def createMaze3():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", "#", "#", "#", "#", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "X", "#"])

    return maze


def printMaze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0

    # set은 순서가없다. 중복된값은 제거
    pos = set()
    
    for move in path:
        print('move:',move)
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()
        


def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        # 범위안에 들었는지만 확인(아예 findEnd할때 한번에 못하나?)
        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True

# moves는 모든경우의 값을 다 가지고 있다. 
# 근데, findEnd끝을 만났을때 출력을 시키면 그 해당값만 출력하니..
# 마치 shortest 으로 간것처럼..실제로도 먼저 끝난패스가 가장빠른거니깐..
def findEnd(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            # 이걸왜하는거지? 첫start를 찾기위해서..
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":
        printMaze(maze, moves)
        return True
    return False


# MAIN ALGORITHM
# 큐는 그냥 하나의 스트링이다. 별거없다.
nums = queue.Queue()
nums.put("")
add = ""
maze  = createMaze2()
# 어떻게 이런생각으로 풀게 되었는지가 가장중요하다.
# 이렇게 while조건식에 함수를 사용하는 경우 어떤경우인가? 
# 그냥 단순하게 그 목적만을 일단 생각하자! findEnd니깐.. 추가된 add가 마지막좌표 X 인지만 확인해서 리턴(True,False)
# 원래 while문에서는 큐,힙에서 실제로 pop을하지않아, 그냥 배열값을 지정하여([i][j]등으로) 값만확인.
while not findEnd(maze, add): 
    # 원래는 nums.get()을 여러번실행하면 queue에 담긴값이 FIFO로 넣은순서대로 나오게 되어있다.
    # https://www.geeksforgeeks.org/queue-in-python/
    # 여기서는 한번만실행했는데, 이유는 그냥 하나에다가 몰빵해서..이럴꺼면 queue를 왜써? 
    # get도 pop처럼 한번 빼면 nums에 변경을 준다(빠진다)
    add = nums.get()

    # 그냥 자유의지로 갈수 있는 한 칸을 임의로 loop를 돈다.
    # 모든경우를 만들게 되겠지..마지막 findEnd일때 출력하면 그걸 만들기 위해 찾은 경로를 출력.
    for j in ["L", "R", "U", "D"]:
        # 몇번을 사용해야 다나오게 할지 모르므로,,그냥 이경우엔 하나의 String으로 처리를 한것 같다.(이중배열아닌 단일값이니..가능한것이기도하고)  
        # 결국, 이 케이스에서는 string이나 queue나 다를게 없는거지...
        # 또한 넣을때에 새로넣을값을 앞에넣냐 뒤에넣냐에 따라 값이 달라지게되니..조심(경우에따라 사용하면된다.)
        # basicQueue.py 참고 
        put = add + j
        # 이번에 추가된 경로가 valid 한거냐? 
        # put이 아마도 RRDDLU 뭐 이런식으로 될꺼야...
        if valid(maze, put):
            # 이번에는 valid한데, 다음에는 아니면?
            nums.put(put)

# print(nums.get())
