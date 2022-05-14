word = ["c=","c-","dz=","d-","lj","nj","s=","z="]
data=input()
for i in word:
    data=data.replace(i,'*')
print(len(data))