# Quiz) Write real estate program 

# print Example :
# There are total XXX Units available

# Honolulu Condo Sale 1 mil 2020
# Kapolei House long rent 500k 2007
# Waikiki Apartment rent 2k/1k 2017



class House:
    
    def __init__(self,location , house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
        

    def show_detail(self):
        print( "{0} {1} {2} {3} {4} ".format(self.location, self.house_type, 
            self.deal_type, self.price, self.completion_year))


houses = []
house1 = House("Honolulu", "Condo", "Sale", "1 mil", "2020")
house2 = House("Kapolei", "House", "long rent", "500k", "2007")
house3 = House("Waikiki", "Apartment", "Rent", "2k/1k", "2017")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("There are {0} Units Available".format(len(houses)))
for house in houses:
    house.show_detail()

