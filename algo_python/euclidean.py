
# 최대공약수
# 두 수 a, b (a > b) 가 있다.
# a 나누기 b 의 나머지를 r1 라고 정의한다면
# (a, b) 의 최대공약수는 (b, r1) 의 최대공약수와 동일하다.

# b 나누기 r1 의 나머지를 r2 라고 정의한다면
# (b, r1) 의 최대공약수는 (r1, r2) 의 최대공약수와 동일하다.

# 위의 방법을 반복하여 나머지 rn 이 0이 되었을 때
# 나누는 수가 최대공약수가 된다.
# 24, 4의 최대공약수는 4

def GCD(a,b):
    smaller = min(a,b)
    # print(smaller)
    for i in range(1,smaller+1):
        # a와 b를 완전하게 나눠떨어지는 i 근데, 제일작은거겠다
        if a % i == 0 and b % i == 0:
            result = i
    return result

aa = GCD(100,24)
print(aa)

# 24, 4의 최대공배수는 24*4/4 = 24
def LCM(a,b):
    return a * b / GCD(a,b)

bb = LCM(24,4)
print(bb)    