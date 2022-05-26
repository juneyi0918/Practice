lst=[0]*10
for i in range(10):
    lst[i]=int(input())
print(int(sum(lst)/len(lst)))
print(max(set(lst),key = lst.count))

