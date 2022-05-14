# def profile (name, age, sex, main_lang):
#     print("Name: {0}\t Age: {1}\t Gender: {2}\t main_lang: {3}"\
#         .format(name,age,sex,main_lang))


# profile("June",24,"Male","C++")
# profile("Seung",23,"Male","Java")


def profile (name, age=24, sex="male", main_lang="python"): 
    print("Name: {0}\t Age: {1}\t Gender: {2}\t main_lang: {3}"\
         .format(name,age,sex,main_lang))

profile("June")
profile("Seung")



