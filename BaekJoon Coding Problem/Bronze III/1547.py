M=int(input())
ball=1

for i in range(M):
    X,Y=map(int,input().split())
    if X==ball:
        ball=Y
        continue
        
    if Y==ball:
        ball=X   
        continue

print(ball) 