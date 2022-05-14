limit=int(input())
speed=int(input())
diff= speed-limit

if diff<=0:
    print("Congratulations, you are within the speed limit!")
else:
    if 20>=diff>=1:
        print("You are speeding and your fine is $100.")
    if 30>=diff>=21:
        print("You are speeding and your fine is $270.")
    if diff>=31:
        print("You are speeding and your fine is $500.")