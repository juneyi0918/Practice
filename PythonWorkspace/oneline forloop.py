# # Add 100 for list

# students = [1,2,3,4,5]
# print(students)
# students= [i+100 for i in students]
# print(students)


# # Change student's name to length
# students = ["Iron man", "Thor", "Groot"]
# print(students)
# students =[len(i) for i in students]
# print(students)

# Change students name for upper

students = ["Iron man", "Thor", "Groot"]
students = [i.upper() for i in students]
print(students)


cash = 0

for i in range (10):
    print ("지금 재산은{cash}원 입니다")
    cash = cash + 1
    print(cash) 
     
    