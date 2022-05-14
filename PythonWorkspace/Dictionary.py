# cabinet = { 1:"June", 100:"Seung"}

# print(cabinet[1])
# print(cabinet[100])

# print(cabinet.get(1))
# print(cabinet.get(100))

# print(cabinet.get(2))  # print NONE
# print(cabinet[2]) # ERROR

# print (1 in cabinet)   # True because of 1:"June"
# print (5 in cabinet)   # False becuase 5 is empty


cabinet = { "A-1":"June", "B-100":"Seung"}

print(cabinet["A-1"])
print(cabinet["B-100"])
# print(cabinet.get("A-1"))
# print(cabinet.get("A-2"))


# NEW Customer
print(cabinet)
cabinet["A-1"]= "Jin"
cabinet["C-20"]= "Jin"
cabinet["C-20"]= "Jin"
print(cabinet)


# LEFT Customer

del cabinet["A-1"]
print(cabinet)

# Print only KEY

print(cabinet.keys())

# Print only VALUE

print(cabinet.values())

# Print KEY & VALUE

print(cabinet.items())

# Empty Cabinet :(

cabinet.clear()
print(cabinet)














