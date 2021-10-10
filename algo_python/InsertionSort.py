

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j] :
            print(j, key, arr[j])
            arr[j+1] = arr[j]
            j-=1
            print('----')
        arr[j+1] = key



arr = [3,8,5,7,4]
insertionSort(arr)
# print(arr)
