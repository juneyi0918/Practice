N=int(input())
customer=list(map(int,input().split()))
filled= [0] * 101
reject=0
for i in customer:
    if filled[i]!=0:
        reject+=1
    else:
        filled[i]=1
print(reject) 