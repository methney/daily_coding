# 쪼갤수없는 Fractional Knapsack Problem

def solution(cargo):
    capacity = 15
    pack = []

    for i in range(len(cargo)+1): #+1은 짐이 없는 경우의 수(근데 왜 하필 loop문으로?) 
        pack.append([])
        for c in range(capacity + 1): # 무게를 kg단위로 나눠서 처리? 
            if i==0 or c==0:
                pack[i].append(0)
            elif cargo[i-1][1] <= c: # 일단 가방에 넣을수 있는 가능한 무게안에서...
                pack[i].append(
                    max(
                        cargo[i-1][0] + pack[i-1][c-cargo[i-1][1]],
                        pack[i-1][c]
                    )
                )
            else: # 가방에 넣을수 없는 경우의 무게 
                pack[i].append(pack[i-1][c])

    return pack[-1][-1]


cargo = [
    (4,12),
    (2,1),
    (10,4),
    (1,1),
    (2,2)
]

solution(cargo)