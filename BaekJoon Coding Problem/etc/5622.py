word=input().upper()
word_list= ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
cnt=0

for unit in word_list:
    for i in unit:
        for x in word:
            if i==x:
                cnt= cnt + word_list.index(unit)+3
print(cnt)