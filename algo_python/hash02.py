# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 같은 전화번호가 중복해서 들어있지 않습니다.

# import re 
def solution(phone_book):
    # newList = []

    # if len(phone_book) > 1000000:
    #     return -1

    # for x in phone_book:
    #     if len(x) > 20 :
    #         return -1
    #     if len(newList) == 0:
    #         pattern = '^'+x+'\d+'
    #         r = re.compile(pattern)
    #         newList = list(filter(r.match,phone_book))
    # return False if len(newList)>0 else True

    # --------------------------
    # bubble sort 방식으로 처리하기 (효율성에서 탈락됨)
    # ret = True
    # phone_book.sort()
    # for x in range(len(phone_book)-1):
    #     pattern = '^' + phone_book[x] + '\d+'
    #     # if ret and phone_book[x+1].find(phone_book[x])!=-1:
    #     if ret and re.search(pattern, phone_book[x+1]):
    #         ret = False

    # return ret

    # ---------------------------

    # bubble sort 방식으로 처리하기 (효율성에서 탈락됨)
    # find는 발견하면 index없으면 -1

    ret = True
    phone_book.sort()
    for x in range(len(phone_book)-1):
        if ret and phone_book[x+1].find(phone_book[x])==0: # 여기서 0이라는거 자체가 첫번째항목을 말함 > 따라서 위와 같이 정규식 안해도된다.
            ret = False
    return ret

    # ----------------------------
    # 풀이에 있었던 방식 

    # answer = True
    # phone_book.sort()
    # book_len = len(phone_book)
    # for i in range(book_len):
    #     if i+1 >= book_len:
    #         break

    #     if len(phone_book[i+1]) > len(phone_book[i]) :
    #         if phone_book[i+1].find(phone_book[i]) == 0 :
    #             return False

    # return True



phone_book = ["119", "97674223", "1195524421"]
# phone_book = ["123","456","789"]
# phone_book = ["12","123","1235","567","88"]

print(solution(phone_book))



