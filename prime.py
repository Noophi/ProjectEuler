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
    sqrt = int(num**0.5)

    #가진 리스트로 판별 가능한 경우
    if plist[-1] >= num:
        for p in plist:
            if p > sqrt:
                break 
            l.append(p)
        return l
    #가진 리스트로 판별 불가능한 경우
    else:
        add_primes(num)
        return plist

def isprime(num): #소수일 땐 True를 리턴하고, 소수가 아닐 땐 False를 리턴
    #가진 소수 리스트가 판별하려는 수를 넘을 경우, 리스트와 직접 비교하여 바로 판별
    if plist[-1]>=num:
        for p in plist:
            if p==num:
                return True
        return False

    #나머지 경우는 적절한 리스트를 가져와서 판별
    else:
        primes = get_proper_plist(num)
        for p in primes:
            if num%p==0:
                return False
        return True

if __name__ == "__main__":
    pass