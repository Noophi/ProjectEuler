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

# 숫자계산으로 자릿수를 바꿔주는 방법: 25초
def rotate_cal(num): # 일의자리를 빼서 가장 높은자리로 올려주는 함수.
    digits = list() # 1. num을 1의자리부터 digits 리스트로 바꿔서 대입
    while num >=1:
       digit = num%10
       digits.append(digit)
       num //= 10
    
    digits.append(digits.pop(0)) # 2. 1의 자리를 빼서 가장 높은자리로 올림
    i=0
    value=0
    for digit in digits:
        value+=digit*10**i
        i+=1

    return value

# 문자열로 변환하여 자리를 바꿔주는 방법: 22초
def rotate_str(num):
    s = str(num)
    val = s[-1] + s[:-1]
    n = int(val)
    return n

def is_circular_prime(num):
    # num이 소수가 아니라면 바로 끝냄
    if p(num)==False: return False
    length = len(str(num))
    for i in range(1, length):
        num = rotate_str(num)
        if p(num)==False: return False
    return True

def has_zero(num):
    string = str(num)
    length = len(string)
    for i in range(0, length):
        if string[i]=='0':
            return True
    return False

count=0
for i in range(1, 1000000):
    if has_zero(i)==False and is_circular_prime(i) == True: count+=1

print(count)
print(time.time()-s)