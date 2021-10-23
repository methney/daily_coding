

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j] :
            print(i,'/', j, ':', key, '<', arr[j])
            arr[j+1],arr[j] = arr[j],arr[j+1]
            j-=1
            print('----')
            getList(arr)
        arr[j+1] = key

def getList(a:list):
    for i in a:
        print(i)


arr = [3,8,5,7,4]
insertionSort(arr)
print(arr)
