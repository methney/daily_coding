# 쪼갤수없는 Fractional Knapsack Problem
# 쪼갤수있는 문제는 탐욕그리디 알고리즘, 이거는 그냥 하위순환(Recursive)로 대응이라고 하는데..타뷸레이션이래..(6X16) = (가방+1) X (냅색허용량+1)
# 여기서는 뭐..recursive한거는 없는것 같은데?

def solution(cargo):
    capacity = 15 #15kg
    pack = []

    # 6 X 16의 경우의수...
    for i in range(len(cargo)+1): #+1은 짐이 없는 경우의 수(근데 왜 하필 loop문으로?) 
        pack.append([])
        for c in range(capacity + 1): # 무게를 kg단위로 나눠서 처리? 
            if i==0 or c==0:
                pack[i].append(0)
            elif cargo[i-1][1] <= c: # 일단 가방에 넣을수 있는 가능한 무게안에서...최대값
                pack[i].append(
                    max(
                        cargo[i-1][0] + pack[i-1][c-cargo[i-1][1]],
                        pack[i-1][c]
                    )
                )
                # 경우의 수
                # i = 0, c = 0
                # cargo[0][0] > (4,12)에서 4
                # pack[0][1-cargo[0][1]] 에서 cargo[0][1] > (2,1) 에서 1 이니깐.. pack[0][1]
                # cargo[i-1][0] + pack[i-1][c-cargo[i-1][1]] >>> 4 + pack[0][1] 이고
                # 아래에 pack[0][1] 결국, max(pack[0][1],pack[0][1]) 로 같다. 그럼 pack[1].append(pack[0][1]) 이거야? 
                # 이게..뭐야? 쪼갤수있는 문제다 잘 풀자...
                # 결국이건 책에 있는 타뷸레이션이라는거(행렬) 이걸 이해해야 할것 같아.
                # 책을 봐도 뭔소린지 모르겠다..씨바..


            else: # 가방에 넣을수 없는 경우의 무게 
                pack[i].append(pack[i-1][c])

    return pack[-1][-1]

# ($4 12kg)...
cargo = [
    (4,12),
    (2,1),
    (10,4),
    (1,1),
    (2,2)
]

print(cargo[0][1])


# solution(cargo)