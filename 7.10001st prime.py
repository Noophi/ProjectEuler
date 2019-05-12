import prime, time
s=time.time()
p = prime

l=[2,3]
i=3
while len(l)!=10001:
    i+=2
    if p.isprime(i)==True:
        l.append(p)

print(time.time()-s)