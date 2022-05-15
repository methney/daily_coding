# 쪼갤수있는 Fractional Knapsack Problem
# 그리디알고리즘(눈앞의 최고이익에 집착)
# 최고가치순으로 일단 정렬하고, 못넣으면 쪼개서라도 넣는다.

def solution(cargo):
    capacity = 5 #kg
    pack = []

    # 단가계산 역순정렬
    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1])) # 무게별단가순으로 뭘하려는 모양이그만...
    pack.sort(reverse=True); # 단가높은순으로 정렬

    # 단가순 그리디 계산
    total_value: float = 0
    for p in pack:
        if capacity - p[2] >= 0: # 가방에 짐이 들어간다면, 
            capacity -= p[2]
            total_value += p[1]
        else :
            # 뭐야이건? 짐이 가방보다크면, 가방을 짐의무게로 나눠? (쪼개는거야?)
            # 예를들면 가방(capacity)가 5인데, 짐이 10이야.. 5/10 = 0.5, 짐의가치가 $1이라면, 
            # total_value는 1 * 0.5 = 0.5이네...(그만큼의가치계산이고만..)
            fraction = capacity / p[2]  
            total_value += p[1] * fraction
            break
    return total_value
 
   


# ($4 12kg)...
cargo = [
    (4,12),
    (2,1),
    (10,4),
    (1,1),
    (2,2)
]

print(solution(cargo))
