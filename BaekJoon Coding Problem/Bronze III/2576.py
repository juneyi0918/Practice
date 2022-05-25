odd=[]
for i in range(7):
    n=int(input())
    if n%2==1:
        odd.append(n)
    else:
        continue
if len(odd)>=1:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)