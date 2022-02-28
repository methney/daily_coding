# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.
# 입출력 예
# participant	completion	return
# ["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
# ["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
# ["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"


# ------------ dictionary, list ---------------
# 
# key가 'p'인 값을 구하는 방법 d.get('p') 
# 'z'가 없을때, 초기값설정 0으로 하면 d.get('z',0) 
# 
# [x for x in d if d[x]>0] 이렇게 간단하게 필터링 map함수를 안써도 된다.
# 
# ---------------------------------------------

# ------------ 쌍이 있는 경우는 stack으로 처리 ---------------
# 
# valid parenthesis 
# 쌍이 아닌 경우, 하단과 같이 그냥 dict 과 d.get('p',0)+1 로 처리(개수를 세는 경우)
# 
# ---------------------------------------------

import copy
import collections

def solution(participant, completion):
    # a = copy.copy(participant)
    # for p in participant :
    #     if p in completion :
    #         a.remove(p)
    # return a[0] if len(a) else ''

    # list 선언은 d=dict() 
    # 리스트이름의 값을 구하는 방법 d.get(p) 인데, 초기값설정 0으로 하면 d.get(p,0)
    d = {}
    # d = dict() 동일하다.
    for p in participant:
        d[p] = d.get(p,0)+1
    for c in completion:
        d[c] -= 1

    # list에서 이름과 값을 리스트컴프리핸션으로 빼내는 방법
    # for k,v in d.items():
    #     print(k,'/',v)
    # return list(k for k,v in d.items() if v==1).pop()

    re = [x for x in d if d[x]>0]
    return re[0] if len(re)>0 else ''

# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))