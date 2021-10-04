

arr = [5, 4, 7, 8, 2, 6, 1, 3]


def printf(arr):
    for i in arr:
        print(i)

# dynamic으로 할것인가? 
def mergeSort(arr):
    if len(arr) < 2:
        return arr

    # 여기부터 아래 dp 부분까지를 반복하면 1개의 배열까지 다 쪼갠다. 
    mid = len(arr)//2 #position

    # 아래 dp으로 작성을 생각하지 못했다. 
    arr_lower = mergeSort(arr[:mid])
    arr_high = mergeSort(arr[mid:]) # 여기를 :mid 로 실수했다. 

    arr_merge = []
    l = h = 0

    # 여기를 돌면서, 쪼갠 배열을 머지한다. 
    while l < len(arr_lower) and h < len(arr_high) :
        if arr_lower[l] < arr_high[h]:
            arr_merge.append(arr_lower[l])
            l+=1
        else :
            arr_merge.append(arr_high[h])
            h+=1

    arr_merge += arr_lower[l:]
    arr_merge += arr_high[h:]

    return arr_merge 

arr = mergeSort(arr)
printf(arr)










