N=int(input())
cnt=1
space=0
for i in range(1,N+1):
    print(' '*space+'*'*(2*N-cnt))
    cnt+=2
    space+=1
for j in range(1,N):
    print(' '*(N-j-1)+'*'*(2*j+1))