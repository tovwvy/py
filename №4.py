class House:
    def look(self):
        return "This is a generic house."


class With_land(House):
    def look(self):
        return "This is a house with land."


class Without_land(House):
    def look(self):
        return "This is a house without land."


class For_many_families(House):
    def look(self):
        return "This is a house for many families."


class For_one_family(House):
    def look(self):
        return "This is a house for one family."


class Villets(With_land, Without_land):
    pass


class Apartments(For_many_families, For_one_family):
    pass


# Creating objects
villets_house = Villets()
apartments_house = Apartments()

# Calling handlers
print(villets_house.look())  # Output depends on MRO: Without_land -> With_land
print(apartments_house.look())  # Output depends on MRO: For_one_family -> For_many_families
