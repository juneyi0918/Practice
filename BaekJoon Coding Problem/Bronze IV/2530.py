A,B,C=map(int,input().split())
D=int(input())
T=A*3600+B*60+C+D
print (T//3600%24,T//60%60,T%60)
