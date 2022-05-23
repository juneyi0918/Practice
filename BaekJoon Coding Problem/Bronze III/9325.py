T=int(input())
for _ in range(T):
    s=int(input())
    n=int(input())
    lst=[s]
    for i in range(n):
        q,p=map(int,input().split())
        price=q*p
        lst.append(price)
    print(sum(lst))