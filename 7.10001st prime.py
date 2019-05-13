import prime, time
s=time.time()
p = prime


l=[2,3]
# 2를 제외하고 짝수는 소수가 아니므로, 3부터 +2씩 증가하며 판단하는게 빠름
# 물론 isprime함수에서 가장 먼저 2로 나누어보지만, 그래도 애초에 안 나눠보는게 20% 정도 속도 빨라짐

i=3
while len(l)!=10001:
    i+=2
    if p.isprime(i)==True: l.append(i)

print(i)

print(time.time()-s)