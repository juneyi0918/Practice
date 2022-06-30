vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

for _ in range(int(input())):
    sentence=input()
    c=v=0
    for i in sentence:
        if i in vowels:
            v+=1
        elif i.isalpha():
            c+=1
    print(c,v)
