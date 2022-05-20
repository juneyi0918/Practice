T=int(input())
for i in range(T):
    N=int(input())
    school={}
    for j in range(N):
        a,b=input().split()
        school[a]=int(b)
    yangjojang=max(school,key=school.get) 
    print(yangjojang)