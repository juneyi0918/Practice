M=int(input())
N=int(input())
prime=[]
for i in range(M,N+1):
    if i>1:
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            prime.append(i)
    else:
        continue
if len(prime)>=1:
    print(sum(prime))
    print(min(prime))
else:
    print(-1)