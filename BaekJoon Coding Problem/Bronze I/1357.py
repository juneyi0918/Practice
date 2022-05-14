X,Y=map(int,input().split())
revX=str(X)[::-1]
revY=str(Y)[::-1]
sum=int(revX)+int(revY)
revsum=str(sum)[::-1]

print(int(revsum))
