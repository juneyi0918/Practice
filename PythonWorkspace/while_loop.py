#how to use while loop


# customer = "Thor"
# index = 5
# while index >= 1:
#     print("{0}, Coffee is ready. {1} left".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("your Coffee is trashed :(")



# customer = "Iron Man"
# index = 1
# while True:
#     print("{0}, your coffee is ready. Called {1} times".format(customer, index))
#     index += 1

customer = "Thor"
person = "Unknown"

while customer != person:
    print("{0}, your coffee is ready".format(customer))
    person = (input("what is your name? "))
    