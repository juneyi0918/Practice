N=int(input())
lst=[]
ans=[]
for i in range(N):
    player=str(input())
    player=player[0]
    lst.append(player)
for k in range(N):
    if lst.count(lst[k])>=5:
        ans.append(lst[k])
ans= list(set(ans))
# ans=sorted(ans)
ans.sort()

if len(ans)==0:
    print("PREDAJA")
else:
    print("".join(ans))

    


# print(lst)