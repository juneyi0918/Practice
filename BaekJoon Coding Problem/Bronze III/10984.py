T=int(input())
for _ in range(T):
    N=int(input())
    avg=0
    tot=0
    c_tot=0
    for _ in range(N):
        c,g=input().split()
        c=int(c)
        g=float(g)
        c_tot+=c
        tot+=c*g
    ans=tot/c_tot
    ans=round(ans,1)
    print(c_tot,ans)