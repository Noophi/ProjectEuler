'''
The number 3797 has an interesting property. 
Being prime itself,
it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes
that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

import time, prime
s=time.time()
p=prime.isprime

def is_trunc(num): # num을 string으로 전환해서 문자열 추출을 통해 판단
    length = len(str(num))-1

    # 우측에서 하나씩 숫자 제거
    i=0
    string = str(num)
    while i < length:
        string = string[:-1]
        if p(int(string))==False: return False
        i+=1
    
    # 좌측에서 하나씩 숫자 제거 
    i=0
    string = str(num)
    while i < length:
        string = string[1:]
        if p(int(string))==False: return False
        i+=1

    return True

trunc = list()
i=11
while len(trunc) < 11:
    if p(i) == True and is_trunc(i)==True: trunc.append(i)
    i+=1
print(trunc)

total = 0
for num in trunc: total += num
print(total)

print(time.time()-s)