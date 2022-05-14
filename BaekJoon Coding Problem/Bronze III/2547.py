T=int(input())
for i in range(T):
    lst=[]
    q=input()
    c=int(input())
    for _ in range(c):
        candy=int(input())
        lst.append(candy)
    print ("YES" if sum(lst)%c==0 else "NO")
        