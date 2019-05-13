'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

import prime, time

p = prime.isprime
s = time.time()

#2는 애초에 넣어놓고, 3부터 +2씩하면서 소수를 찾는 계산이 30%정도 빠름
i=3
sum=2
while i<2000000:
    if p(i)==True : sum+=i
    i+=2

print(sum)
print(time.time()-s)