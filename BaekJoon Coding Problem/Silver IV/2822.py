lst=[]
for i in range(8):
    n=int(input())
    lst.append(n)
sorted_lst=sorted(lst,reverse=True)
t=sum(sorted_lst[:5])
idx_lst=sorted(lst.index(sorted_lst[i])+1 for i in range(5))
print(t)
print(*idx_lst)