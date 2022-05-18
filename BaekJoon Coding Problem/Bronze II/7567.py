lst=list(map(str,input()))
ans=0
for i in range(len(lst)):
    if i ==0:
        ans+=10
    elif lst[i]==lst[i-1]:
        ans+=5
    else:
        ans+=10
print(ans)
