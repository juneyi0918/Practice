# SET
# Can not Overlap, No order

my_set = {1,2,3,3,3}
print(my_set)


java = {"June", "Seung", "Jin"}
python = set(["June","Brian"])

# Find intersection (java & python)

print (java & python)
print (java.intersection(python))


#  Find union  ( java or python )

print (java | python)
print (java.union(python))

# Find difference ( only java not python)

print( java - python)
print(java.difference(python))


# ADD new value in the set

python.add("Seung")
print(python)

# Delete old value in the set

java.remove("Jin")
print(java)

