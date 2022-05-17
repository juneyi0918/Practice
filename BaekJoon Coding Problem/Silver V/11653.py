N=int(input())
factor=2
while N!=1:
    if N%factor==0:
        N=N/factor
        print(factor)
    else:
        factor+=1