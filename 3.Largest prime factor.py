'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143
'''
import time, prime
n=600851475143

s=time.time()
p=prime.isprime

d = 1
while d<n :
    d+=1
    while n%d==0:
        n/=d
    
print(d)
print(time.time()-s)        
        
    