'''
중요 함수
isprime(num) -> return True/False
'''


#소수 리스트 cache
plist = [2,3]

# 알고 있는 소수 중 가장 큰 값+1부터, \sqrt(num)의 정수까지 소수인지 판별
# 다음 버전에는 에라토스테네스 체 구현해볼까
def add_primes(num):
    min = plist[-1]
    max = int(num**0.5)
    for i in range(min+1, max+1):
        if isprime(i) == True:
            plist.append(i)

#알고 있는 소수 리스트로 바로 판별 가능한 경우와, 소수 리스트를 추가해와야 하는 경우로 나뉜다.
def get_proper_plist(num):
    l=list()

    #가진 리스트로 판별 가능한 경우
    if plist[-1] >= num:
        for p in plist:
            if p*p > num:
                break 
            l.append(p)
        return l
    #가진 리스트로 판별 불가능한 경우
    else:
        add_primes(num)
        return plist

def isprime(num): #소수일 땐 True를 리턴하고, 소수가 아닐 땐 False를 리턴
    l=list()
    #가진 소수 리스트가 판별하려는 수를 넘을 경우, 리스트와 직접 비교하여 바로 판별
    if plist[-1]>=num:
        for p in plist:
            if p==num:
                return True
        return False
    #가진 리스트로 판별 가능한 경우
    elif plist[-1]**2 >= num:
        sqrt = int(num**0.5)
        for p in plist:
            if p>sqrt:
                return True
            elif num%p==0:
                return False
    # 소수를 추가해와야하는 경우
    else:
        # 일단 가진거라도 먼저 판단해서 합성수 제외
        for p in plist:
            if num%p==0:
                return False
        
        # 가장큰소수+1 부터, ㅜ\sqrt{num}까지는 소수를 추가해가면서 판단
        min = plist[-1]
        max = int(num**0.5)
        for i in range(min+1, max+1):
            if isprime(i) == True:
                plist.append(i)
                if num%i==0:
                    return False
        return True

        

msg = isprime(101)
print(msg)

if __name__ == "__main__":
    pass