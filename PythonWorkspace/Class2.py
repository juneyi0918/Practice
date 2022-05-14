class Unit:
    def __init__(self):
        print("Unit Creator")

class Flyable:
    def __init__(self):
        print("Flyable Creator")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)


dropship = FlyableUnit()
