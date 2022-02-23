
# Bubblesort
# 5 4 7 8 2 4 1 3

arr = [5, 4, 7, 8, 2, 6, 1, 3]

# 출력을 위한..
def printVal(arr):
    for i in range(len(arr)):
        # print(i)
        print(arr[i])
    print('------')

def bubbleSort(arr):
    l = end = len(arr)
    # How1.
    for i in range(l-1,0,-1):    
        for j in range(i):
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]

    # How2.
    # while end > 0 :
    #     swap = False
    #     for i in range(end-1):
    #         if arr[i] > arr[i+1]:
    #             arr[i], arr[i+1] = arr[i+1], arr[i]
    #             swap = True
    #     if not swap :
    #         break 
    #     end -= 1
    
    return arr

bubbleSort(arr)
# printVal(arr)

