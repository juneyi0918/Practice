N=int(input())
list=[]
for i in range (N):
    list.append(int(input()))
    
list.sort()
print(*list,sep="\n")

