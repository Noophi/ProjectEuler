import prime, time
s=time.time()
p = prime

l=[2]
i=2
while len(l)!=10001:
    i+=1
    if p.isprime(i)==True:
        l.append(i)

print(i)

print(time.time()-s)