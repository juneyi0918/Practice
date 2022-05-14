import sys
N=int(sys.stdin.readline())  # input -> sys.stdin.readline()
lst=[]
for i in range(N):
    M=int(sys.stdin.readline())
    lst.append(M)
    
print(sum(lst)-N+1)