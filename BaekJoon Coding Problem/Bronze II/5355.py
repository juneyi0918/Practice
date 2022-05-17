T=int(input())

for i in range(T):
    lst=list(map(str,input().split()))
    ans=0
    for j in range(len(lst)):
        if j==0:
            ans=float(lst[j])
        elif lst[j]=='#':
            ans-=7
        elif lst[j]=='%':
            ans+=5
        elif lst[j]=='@':
            ans*=3
           
    print("%0.2f"% ans)