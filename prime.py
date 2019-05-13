'''
중요 함수
isprime(num) -> return True/False
'''

#소수 리스트 cache
plist = [2,3]

def isprime(num): #소수일 땐 True를 리턴하고, 소수가 아닐 땐 False를 리턴
    #가진 소수 리스트가 판별하려는 수를 넘을 경우, 리스트와 직접 비교하여 바로 판별
    if plist[-1]>=num:
        for p in plist:
            if p==num: return True
        return False
    #가진 리스트로 판별 가능한 경우
    elif plist[-1]**2 >= num:
        sqrt = int(num**0.5)
        for p in plist:
            if p>sqrt: return True
            elif num%p==0: return False
    # 소수를 추가해와야하는 경우
    else:
        # 일단 가진 리스트로 먼저 나눠봄.
        for p in plist:
            if num%p==0: return False
        
        # 알고 있는 가장큰소수+1 부터, ㅜ\sqrt{num}까지는 소수를 추가해가면서 판단
        # 알고 있는 가장 큰 소수를 k라 하면,
        # k > 2 일 때, k~2k 사이에는 반드시 소수가 하나 존재함이 알려져있고
        # k > 2 일 때, k^2 > 2k 이므로,
        # 굳이 max = \sqrt{num} 로 두지 않아도 소수를 찾아낼 수 있다. (10%정도 시간단축됨)
        min = plist[-1]
        max = min*2
        for i in range(min+1, max):
            if isprime(i) == True:
                plist.append(i)
                if num%i==0: return False # 만일 추가한 소수의 배수라면, 바로 합성수임을 리턴
        return True

if __name__ == "__main__":
    pass