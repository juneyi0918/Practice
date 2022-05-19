N=int(input())
lst=[]
for i in range(N):
    n=int(input())
    lst.append(n)
if lst.count(1)>lst.count(0):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")