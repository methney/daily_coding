
def is_prime(num):
    if num <= 1: 
        return False
    # 약수가 없는 수 
    for i in range(2,num):
        if num%i==0 : 
            return False
    return True

print(is_prime(6))
print(is_prime(5))

