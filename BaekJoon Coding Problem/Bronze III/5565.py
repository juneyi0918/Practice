total=0
lst=[]
for i in range(10):
    n=int(input())
    if i==0:
        total=n
    else:
        lst.append(n)
print(total-sum(lst))