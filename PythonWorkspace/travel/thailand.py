class ThailandPackage:
    def detail(self):
        print("[Thailand Package]: Bangkok, Pataya tour : $500")

if __name__ == "__main__":
    print("Thailand module is use directly")
    trip_to = ThailandPackage()
    trip_to.detail()

else:
    print("module used outside")
