n=int(input())
lst=[0, 1, 1]
for i in range(3,n+1):
   new=lst[i-1]+lst[i-2]
   lst.append(new)
print(lst[n])