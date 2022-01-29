import queue

# https://www.techwithtim.net/tutorials/breadth-first-search/
# BFS로 미로찾는 아주 간단하고 좋은예


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


def printMaze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
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

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True


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
        print("Found: " + moves)
        printMaze(maze, moves)
        return True

    return False


# MAIN ALGORITHM
# 큐는 그냥 하나의 스트링이다. 별거없다.
nums = queue.Queue()
nums.put("")
# print('--',nums)
add = ""
maze  = createMaze2()

# will next row and column is valid in maze then keep going
while not findEnd(maze, add): 
    # 원래는 nums.get()을 여러번실행하면 queue에 담긴값이 FIFO로 넣은순서대로 나오게 되어있다.
    # https://www.geeksforgeeks.org/queue-in-python/
    # 여기서는 한번만실행했는데, 이유는 그냥 하나에다가 몰빵해서..이럴꺼면 queue를 왜써? 
    
    add = nums.get()
    # print('---', add)
    for j in ["L", "R", "U", "D"]:
        # 몇번을 사용해야 다나오게 할지 모르므로,,그냥 이경우엔 하나의 String으로 처리를 한것 같다.  
        # 결국, 이 케이스에서는 string이나 queue나 다를게 없는거지...
        # 또한 넣을때에 새로넣을값을 앞에넣냐 뒤에넣냐에 따라 값이 달라지게되니..조심(경우에따라 사용하면된다.)
        # basicQueue.py 참고 
        put = add + j
        # 이번에 추가된 경로가 valid 한거냐? 
        # put이 아마도 RRDDLU 뭐 이런식으로 될꺼야...
        if valid(maze, put):
            nums.put(put)




# test = queue.Queue()
# test.put("a")
# test.put('b')

# # 넣은순서대로 나온다. queue니깐...
# print(test.get())
# print(test.get())
