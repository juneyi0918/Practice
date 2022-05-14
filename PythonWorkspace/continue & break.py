absent =[2,5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("This is it. {0}, you need to see me after class".format(student))
        break
    print("{0}, Please read page {0}".format(student))
