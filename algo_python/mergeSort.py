

arr = [5, 4, 7, 8, 2, 6, 1, 3]

# [5,4,7,8][2,6,1,3]
# [5,4][7,8][2,6][1,3]
# [5][4][7][8][2][6][1][3]
'''
compare: 5 4
s---- [4] [5] []
e---- [4, 5]
compare: 7 8
s---- [7] [] [8]
e---- [7, 8]
compare: 4 7
compare: 5 7
s---- [4, 5] [] [7, 8]
e---- [4, 5, 7, 8]
compare: 2 6
s---- [2] [] [6]
e---- [2, 6]
compare: 1 3
s---- [1] [] [3]
e---- [1, 3]
compare: 2 1
compare: 2 3
compare: 6 3
s---- [1, 2, 3] [6] []
e---- [1, 2, 3, 6]
compare: 4 1
compare: 4 2
compare: 4 3
compare: 4 6
compare: 5 6
compare: 7 6
s---- [1, 2, 3, 4, 5, 6] [7, 8] []
e---- [1, 2, 3, 4, 5, 6, 7, 8]
'''

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
    # 일단 이 부분에서 recursive하게 쪼갠다.(하나될때까지..)
    arr_lower = mergeSort(arr[:mid])
    arr_high = mergeSort(arr[mid:]) # 여기를 :mid 로 실수했다. 

    arr_merge = []
    l = h = 0

    # 여기를 돌면서, 쪼갠 배열을 머지한다.
    # 여기서는 비교하는 둘중에 작은것을 먼저 arr_merge 배열에 담는다. 5 < 4 
    # 이 조건이 이해가 잘안된다(바뀌는 것은 l,h)
    while l < len(arr_lower) and h < len(arr_high) :
        # print('compare:',arr_lower[l],arr_high[h],'/', arr_lower, arr_high, arr_merge)
        if arr_lower[l] < arr_high[h]:
            arr_merge.append(arr_lower[l])
            l+=1
        else :
            arr_merge.append(arr_high[h])
            h+=1

    # 아래부분이 이해가 안갔다. 위에서는 비교하는 둘중에 작은넘을 arr_merge에 넣는다. 4,5라면 여기서는 arr_merge에 4만 넣는다.
    # 5를 넣는 부분은 아래에서 처리한다. 
    # print('s----', arr_merge, arr_lower[l:], arr_high[h:])
    arr_merge += arr_lower[l:]
    arr_merge += arr_high[h:]
    # print('e----', arr_merge)

    return arr_merge 

mergeSort(arr)










