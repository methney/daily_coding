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

def solution(genres, plays):
    answer = []
    from collections import defaultdict
    s = defaultdict(dict) # classic: [곡 인덱스]
    s_num = defaultdict(int) # 장르별 플레이합산 저장
    # Zip은 같은 배열크기일때, 하나씩 빼서 나래비 세워줌
    for g,(idx,p) in zip(genres, enumerate(plays)):
        s[g][idx] = p
        s_num[g] += p

    print(s) # {'classic': {0: 500, 2: 150, 3: 800}, 'pop': {1: 600, 4: 2500}}) 
    print(s_num) # {'classic': 1450, 'pop': 3100})
    s_num = [k for k,v in sorted(s_num.items(), key= lambda items: items[1], reverse=True)]
    print(s_num)

    for g in s_num:
        answer.extend([k for k,v in sorted(s[g].items(), key= lambda items: items[1], reverse=True)][:2]) # 두개씩모아 베스트앨범을 출시하려고 합니...
    print(answer) # [4,1,3,0]
    return answer

# ---------------------------------

# def solution(g,p):
    # for i in enumerate(p):
    #     print(i)
    # 다행1열의 배열을 enumerate 출력하면, 다음과 같이 출력
    # (0, 500)
    # (1, 600)
    # (2, 150)
    # (3, 800)


# def solution(g,p):


genres = ["classic", "pop", "classic", "classic", "pop"]	
plays = [500, 600, 150, 800, 2500]

solution(genres, plays)
