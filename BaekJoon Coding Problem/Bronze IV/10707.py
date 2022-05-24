A=int(input())
B=int(input())
C=int(input())
D=int(input())
P=int(input())
X=P*A
if P<=C:
    Y=B
else:
    Y=B+(P-C)*D
print(min(X,Y))