people_list=[]
people=0
for i in range(4):
    A,B=map(int,input().split())
    people-=A
    people+=B
    people_list.append(people)
print(max(people_list))