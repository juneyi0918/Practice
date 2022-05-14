e,f,c=map(int,input().split())
bottle=e+f
ans=0
while bottle>=c:
   ans+=bottle//c
   bottle=bottle//c+bottle%c
print(ans) 