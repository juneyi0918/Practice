# Make Password for Different Site Domain.


# ex) http://naver.com
# Rule 1: Delete http://
# Rule 2: Delete .com
# Rule 3: use first 3 characters + number of left letters + number of 'e' + "!"
# Correct Password for example = nav51!


# Domain = "http://naver.com"
Domain = "http://youtube.com"

my_str = Domain.replace("http://", "")
# print(my_str)
my_str = my_str[:my_str.index(".")]
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print (password)
print ("{0}'s password is {1}".format(Domain,password))


