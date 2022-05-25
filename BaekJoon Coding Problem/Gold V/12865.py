## 0-1 Knapsack Problem  -> Dynamic programming

N,K=map(int,input().split())
bag=[[0,0]]  
for i in range(N):
    W,V=map(int,input().split())
    
    