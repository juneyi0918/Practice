lst=[]
for _ in range(int(input())):
    n,d,m,y=input().split()
    lst.append([n,int(d),int(m),int(y)])
lst.sort(key=lambda x:(x[3],x[2],x[1]))
print(lst[-1][0])
print(lst[0][0])