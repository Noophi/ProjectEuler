plist = [2]

def has_enough_prime_list(num):
    pass

def get_enough_prime(num):
    pass

def get_proper_plist(num):
    if plist[-1]**2 >= num:

def isprime(num): #소수일 땐 True를 리턴하고, 소수가 아닐 땐 False를 리턴
    l = get_proper_plist(num)
    if num==2:
        return True

    for p in l:
        if num % p == 0:
            return False
        
    return True

msg = isprime(2)
print(msg)


