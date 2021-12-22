# 로무토파티션이란? 제일오른쪽을 그냥 파티션으로 잡고 시작하는 방법
# 퀵소트가 되려 머지소트보다 코드는 간단하다.
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
    # 피벗은 '값'이다.  
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







