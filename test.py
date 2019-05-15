'''
The number, 197, is called a circular prime
because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

import prime, time
p=prime.isprime
s=time.time()

def num_to_digit(num): #1의자리 숫자부터 리스트로 만듦
    l = list()
    while num >= 1:
        d=num%10
        l.append(d)
        num = int(num/10)
    return l

def rotate_list(set): # 가장 큰 자릿수를 1의자리로 옮기는 회전
    l = list()
    i=-1
    while i < len(set)-1 :
        l.append(set[i])
        i+=1
    return l

def digit_to_num(list): #역순의 숫자 리스트를 숫자로 바꿈.
    number=0
    n=0
    for num in list: 
        number += num*10**n
        n+=1
    return number

def has_zero(num):
    l=num_to_digit(num)
    if 0 in l:
        return True
    return False

def isCircularPrime(num): # 자신이 소수라면, 위의 세 함수를 합성하여 회전한 것도 소수인지 판별
    if p(num)==False or has_zero(num)==True:
        return False
    
    l = len(str(num))
    i=0
    while i < l:
        rotated=digit_to_num(rotate_list(num_to_digit(num)))
        if p(rotated)== False: return False
        i+=1
    return True

msg=p(7111)
print(msg)
'''
count=0
for i in range(1000,10000):
    if isCircularPrime(i)==True:
        count+=1
        print(i)
'''

#print(count)
print(time.time()-s)

        