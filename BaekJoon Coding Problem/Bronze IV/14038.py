cnt=0
for _ in range(6):
    result=input()
    if result=='W':
        cnt+=1

if cnt==6 or cnt==5:
    print(1)
elif cnt==4 or cnt==3:
    print(2)
elif cnt==2 or cnt==1:
    print(3)
else:
    print(-1)