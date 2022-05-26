lst=[]
for i in range(5):
    s1,s2,s3,s4=map(int,input().split())
    sum=s1+s2+s3+s4
    lst.append(sum)
print(lst.index(max(lst))+1,max(lst),sep=' ')