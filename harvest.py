############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, name, code, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""

        self.pairings = []

        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

    def __repr__(self):

        return f"<Melon Name = {self.name}\nMelon Code = {self.code}>"
 

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

    
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType("Muskmelon", "Musk", "1998", "Green", True, True)
    muskmelon.pairings.append("Mint")
    all_melon_types.append(muskmelon)

    casaba = MelonType("Casaba", "cas", "2003", "Orange", False, False)
    casaba.pairings.append("Strawberries, Mint")
    all_melon_types.append(casaba)

    crenshaw = MelonType("Crenshaw", "cren", "1996", "Green", False, False)
    crenshaw.pairings.append("Prosciutto")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType("Yellow Watermelon", "yw", "2013", "Yellow", False, True)
    yellow_watermelon.pairings.append("Ice Cream")
    all_melon_types.append(yellow_watermelon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types: 
        print(f"{melon.name} pairs well with")
        # " ".join(melon.pairings)
        for pairing in melon.pairings:
            print(f"-- {pairing}")

    # def __repr__(self):

    #     print(f"<Melon pairings={self.pairings}")     

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

   
    melon_by_code = {}

    for melon in melon_types:
        melon_by_code[melon.code] = melon

    return melon_by_code

melon_types = make_melon_types() # use the variable on 89 and 90
# print(print_pairing_info(make_melon_types()))
melon_by_id = make_melon_type_lookup(melon_types)

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

    def __init__(self, melon_type, shape_rating, color_rating, harvested_from, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by


    def is_sellable(self):

        if self.shape_rating > 5 and self.color_rating > 5 and self.harvested_from != "Field 3":           
            sellable = True 
        else:        
            sellable = False
        return sellable


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_list = []

    melon_1 = Melon("yw", 8, 7, "Field 2", "Sheila")
    melons_list.append(melon_1)
    melon_2 = Melon("yw", 3, 4, "Field 2", "Sheila")
    melons_list.append(melon_2)
    melon_3 = Melon('yw', 9, 8, "Field 3", "Sheila")
    melons_list.append(melon_3)
    melon_4 = Melon("cas", 10, 6, "Field 35", "Sheila")
    melons_list.append(melon_4)
    melon_5 = Melon("cren", 8, 9, "Field 35", "Michael")
    melons_list.append(melon_5)
    melon_6 = Melon("cren", 8, 2, "Field 35", "Michael")
    melons_list.append(melon_6)
    melon_7 = Melon("cren", 2, 3, "Field 4", "Michael")
    melons_list.append(melon_7)
    melon_8 = Melon("musk", 6, 7, "Field 4", "Michael")
    melons_list.append(melon_8)
    melon_9 = Melon("yw", 7, 10, "Field 3", "Sheila")
    melons_list.append(melon_9)

    return melons_list


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    
    for melon in melons:
        harvested_by = melon.harvested_by
        harvested_from = melon.harvested_from
        is_sellable = melon.is_sellable()
        print(f"Harvested by {harvested_by} from {harvested_from} {is_sellable}")    


melons = make_melons(melon_types)   
print(get_sellability_report(melons))
