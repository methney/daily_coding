# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

# 제한사항
# genres[i]는 고유번호가 i인 노래의 장르입니다.
# plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
# genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
# 장르 종류는 100개 미만입니다.
# 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
# 모든 장르는 재생된 횟수가 다릅니다.
# 입출력 예
# genres	plays	return
# ["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]

# ----------------------------------
# 다른이 풀이 

# def solution(genres, plays):
#     answer = []
#     from collections import defaultdict
#     s = defaultdict(dict) # classic: [곡 인덱스]
#     s_num = defaultdict(int) # 장르별 플레이합산 저장

#     # Zip은 같은 배열크기일때, 하나씩 빼서 나래비 세워줌
#     for g,(idx,p) in zip(genres, enumerate(plays)):
#         s[g][idx] = p
#         s_num[g] += p

#     print(s) # {'classic': {0: 500, 2: 150, 3: 800}, 'pop': {1: 600, 4: 2500}}) 
#     print(s_num) # {'classic': 1450, 'pop': 3100})
#     s_num = [k for k,v in sorted(s_num.items(), key= lambda items: items[1], reverse=True)]
#     print(s_num)

#     for g in s_num:
#         answer.extend([k for k,v in sorted(s[g].items(), key= lambda items: items[1], reverse=True)][:2]) # 두개씩모아 베스트앨범을 출시하려고 합니...
#     print(answer) # [4,1,3,0]
#     return answer


# ------------ nested dict --------------------------------
# 
# 내부에 또 다른 hash형태를 담은 경우(nest) 선언을 아래와 같이..
# collections.defaultdict(dict)
# 
# int 전용으로 사용할 경우에는 
# collections.defaultdict(int) 
# s_num = {}, s_num = dict() 이렇게 하면 에러발생(keyError)
#
# defaultdict과 dict과의 차이점은 (초기값 처리에 대한 유무차이)
# 
# -------------- zip 모줄 ---------------------------------
# 
#  for x,(idx,v) in zip(g, enumerate(p)) 아주 생소하다.
#  키와 값이 분산된 배열을 키 기준으로 모아준다.
#  아래참고 
# 
# ---------------------------------------------------------

import collections
def solution(g, p):
    s = collections.defaultdict(dict)
    s_num = collections.defaultdict(int)
    
    # keyError가 나는 이유는 초기화가 없이 사용하기 때문(없는키를 참조) s_num[x] += v에서 이전값을 참조하기 위해 s_num[x]를 먼저찾기 때문
    # s_num = dict() 
    
    for x,(idx,v) in zip(g, enumerate(p)):
        s[x][idx] = v
        s_num[x] += v 
    # print(s) # {'classic': {0: 500, 2: 150, 3: 800}, 'pop': {1: 600, 4: 2500}}
    # print(s_num) # {'classic': 1450, 'pop': 3100}

    # 아래에서 v를 쓰냐 안쓰냐에 따라, x가 [('pop', 3100), ('classic', 1450)](v안쓸때) 되냐 ['pop', 'classic'](v쓸때) 가 된다
    # 값(v)을 안쓰게되면, 통으로 객체로 리턴해버린다.
    s_num = [x for x,v in sorted(s_num.items(), key=lambda x:x[1], reverse=True)]

    re = []
    for i in s_num : 
        re.extend([x for x,v in sorted(s[i].items(), key=lambda x:x[1], reverse=True)][:2]) # 장르별로 2개씩만 모아...
    return re
    


genres = ["classic", "pop", "classic", "classic", "pop"]	
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))
