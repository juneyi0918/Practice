X=[]
Y=[]
for i in range(3):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)
for j in range(3):
    if X.count(X[j])==1:
        x_ans=X[j]
    if Y.count(Y[j])==1:
        y_ans=Y[j]
print(x_ans,y_ans,sep=" ")
    