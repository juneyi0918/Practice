lst=[]
for i in range(3):    
    a,b,c,d=map(int,input().split())
    sum=a+b+c+d
    if sum==0:
        ans='D'
    elif sum==1:
        ans='C'
    elif sum==2:
        ans='B'
    elif sum==3:
        ans='A'
    else:
        ans='E'
    lst.append(ans)
print(*lst,sep='\n')

    