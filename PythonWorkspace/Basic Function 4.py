# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("Name : {0}\tAge : {1}\t".format(name,age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("Name : {0}\tAge : {1}\t".format(name,age), end=" ")
    for lang in language:               
        print(lang, end=" ")
    print()

profile("June",24,"Python","Java","C","C++","C#","javascript")
profile("Seung",24,"Kotlin","Swift","","","")
