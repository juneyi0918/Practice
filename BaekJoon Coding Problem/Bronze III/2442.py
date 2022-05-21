N=int(input())
star=1
for i in range(1,N+1):
    print(' '*(N-i)+'*'*star)
    star+=2