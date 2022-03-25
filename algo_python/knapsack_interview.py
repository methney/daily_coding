# def knapsack(cargo):
#     capacity = 15
#     pack = []

#     for c in cargo:
#         pack.append([c[0]/c[1], c[0], c[1]])
#     pack.sort(reverse=True)

#     total_value:float = 0
#     for p in pack:
#         if capacity - p[2] >= 0:
#             capacity -= p[2]
#             total_value += p[1]
#         else:
#             fraction = capacity / p[2]
#             total_value += p[1] * fraction 
#             break 

#     return total_value 


# cargo = [(4,12),(2,1),(10,4),(1,1),(2,2)]

# print(knapsack(cargo))


import collections

def knapsack(str):
    list_str = str.rstrip('\r\n').split()
    list_obj = map(int,list_str)
    cargo = list(list_obj)

    cnt_child = cargo[0]
    cnt_present = cargo[1]

    arr_sack = []
    arr_present = []
    for i in range(2, 2+cargo[0]):
        arr_sack.append(cargo[i])    
    for j in range(2+cargo[0],len(cargo)):
        arr_present.append(cargo[j])
    
    present = collections.deque(arr_present)

    able = 'NO'
    
    while len(present) > 0 :
        pop_present = present.popleft()
        no_sack = False
        for sack in arr_sack:
            print(sack,'>=', pop_present)
            if sack >= pop_present : 
                arr_sack = arr_sack[1:]
                no_sack = True
                continue
        if not no_sack:
            present.insert(0,pop_present)
    if len(present) == 0 :
        able = 'YES'
    
    print(able)


# cargo = '5 6 5 3 2 4 1 4 1 4 1 4 1'
cargo = '5 6  5 3 2 4 1  4 1 4 4 1 4'



# user_input = input()
knapsack(cargo)


