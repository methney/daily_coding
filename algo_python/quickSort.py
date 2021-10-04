

arr = [5, 4, 7, 8, 2, 6, 1, 3]


def printf(arr):
    for i in arr:
        print(i)

# dynamic으로 할것인가? 
# input과 output type을 결정
# input : arr(list)
# output : arr(list)
def quickSort(arr):

    if len(arr) <=1 :
        return arr
    pivot = arr[len(arr)//2]
    arr_low, arr_high, arr_mid  = [], [], []
    for num in arr:
        if num < pivot:
            arr_low.append(num)
        elif num > pivot:
            arr_high.append(num)
        else:
            arr_mid.append(num)

    return quickSort(arr_low) + arr_mid + quickSort(arr_high)

arr = quickSort(arr)
printf(arr)









