#  Stupid way.....
# A=int(input())
# B=int(input())
# C=int(input())
# D=int(input())
# E=int(input())

# A=max(40,A)
# B=max(40,B)
# C=max(40,C)
# D=max(40,D)
# E=max(40,E)
# total=A+B+C+D+E
# print(int(total/5))

# much better way....
lst=[]
for i in range(5):
    score= int(input())
    if score<40:
        lst.append(40)
    else:
        lst.append(score)

print(int(sum(lst)/len(lst)))


