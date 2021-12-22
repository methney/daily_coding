

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # i 바로 하나 아래 값과 비교 들어간다.
        
        # i아래에서만 왔다갔다할예정, i값이 커질수록(for에 따라서) 많이 왔다갔다하겠다.
        # 이렇게 제자리를 찾아서 삽입된다고 하여 삽입정렬(insertion Sort)이다.
        while j >= 0 and key < arr[j] : #바로 아래꺼가 더 크다면, 자리바꿔! 
            print(i,'/', j, ':', key, '<', arr[j])
            arr[j+1],arr[j] = arr[j],arr[j+1]
            j-=1
            print('----',j)
        getList(arr)
        # 바로아래 이건왜? for문끝나가는마당에...(빼도영향을 미치지않아..)
        # 만약에 while문이 실행된만큼 j가 줄어들었을텐데..
        # arr[j+1] = key

def getList(a:list):
    for i in a:
        print(i)


arr = [3,8,5,7,4]
insertionSort(arr)
print(arr)
