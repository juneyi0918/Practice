ans=0
for i in range (8):
    lst=list(map(str,input()))
    if i%2==0:
        for j in range (8):
            if j%2==0:
                if lst[j]=='F':
                    ans+=1
    else:
        for k in range(8):
            if k%2==1:
                if lst[k]=='F':
                    ans+=1
print(ans)