# weather = input("How is the weather? ")

# if weather == "rain" or "snow":
#     print("Please prepare umbrella")
# elif weather == "dust":
#     print("Please prepare mask")
# else:
#     print("Weather is good")

temp = int(input ("what is temperature? "))

if temp >= 30:
    print("it is too hot, Don't go outside")
elif  10 <= temp < 30:
    print("it is good weather, you can go outside")
elif 0 <= temp < 10:
    print("kind of cold, bring jacket")
else:
    print("it is way too cold, don't go out")
