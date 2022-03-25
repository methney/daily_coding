# 스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.

# 예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.

# 종류	이름
# 얼굴	동그란 안경, 검정 선글라스
# 상의	파란색 티셔츠
# 하의	청바지
# 겉옷	긴 코트
# 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
# 스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
# 같은 이름을 가진 의상은 존재하지 않습니다.
# clothes의 모든 원소는 문자열로 이루어져 있습니다.
# 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
# 스파이는 하루에 최소 한 개의 의상은 입습니다.
# from itertools import product
# def solution(clothes):
#     return len(list(product(*clothes))) -1

# clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
# solution(clothes)

# ------------ dict 에서 값만으로 loop ---------------
# 
# arr이 dict 형태인데,
# for i in arr.values(): 로 값만으로 배열을 돌릴수 있다. (근데 구지 필요한지는 모르겠다.)
# 
# dict 초기화
# arr.setdefault(i[1],[i[0]]) 구지 이렇게 안해도 되긴해..
# 
# ---------------------------------------------------------

def solution(clothes):
    arr = dict()
    for i in clothes:
        if i[1] in arr: 
            arr[i[1]].append(i[0]) # 종류별로 아이템을 담음(종류가 이미 등록되었다면)
        else :
            arr.setdefault(i[1],[i[0]]) # 새로운종류와 아이템을 담음(이게 안되면 exception 처리를 해줘야한다. defaultdict과 dict차이)
    
    # 새로운 배열선언(아이템 개수등록) 
    v = []
    for i in arr.values():
        v.append(len(i)+1)
    
    # 경우의 수 계산을 위해서
    s = 1
    for i in v:
        s *= i
    
    # 다 벗은경우는 없는 1건은 뺌
    s -= 1
    return s
            
# [아이템,종류] 
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))