
# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if n >= 2:
#         ret = fibo(n-1) + fibo(n-2)
#         print(ret)
#         return ret


# dynamic
def fibo(n):
    
    # d = {0:0, 1:1}
    # 아래처럼하더라도 d는 배열이 아닌 dict타입으로 해야한다.
    d = {} 
    d[0] = 0
    d[1] = 1
    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]

    return d[n]


print(fibo(10))






