# Make program to calculate standard weight

# male: height (m) X height (m) X 22
# female: height (m) X height (m) X 21

#rule #1 : calculate standard weight in side of function
    # function name : std_weight
    # input : height , gender 
#rule #2 : print std weight until 1/100th decimal point

# ex print final = hegiht xxxcm male's standard weight is xx.xx kg. 

def std_weight(height,gender):
    if gender == "male":
        weight = height * height *22
        print("Height {0}cm {1}'s standard weight is {2}kg".format(height*100,gender,round(weight,2)))
    elif gender == "female":
        weight = height * height *21
        print("Height {0}cm {1}'s standard weight is {2}kg".format(height*100,gender,round(weight,2)))
    else:
        print("please only answer as 'male' or 'female'")

std_weight(1.75,"male")
std_weight(1.75,"ts")
std_weight(1.70,"female")
height= float(input("what is your height in meter: "))
gender= input("what is your gender: ")
std_weight(height,gender)
