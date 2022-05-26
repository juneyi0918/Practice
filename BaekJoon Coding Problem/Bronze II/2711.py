T=int(input())
for i in range(T):
    n,word=input().split()
    n=int(n)
    print(word[:n-1],word[n:],sep='')