destinations = ["Paris, France", "Shanghai, China",
                "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


def get_destination_index(destination):
    """This function takes as parameter a destination and returns the index of that destination in the destinations list"""
    return destinations.index(destination)
traveller_destination = test_traveler[1]

def get_traveler_location(traveler):
    """This function takes as parameter a traveler and returns the traveler's location"""
    return traveler[1]

test_destination_index = get_destination_index(get_traveler_location(test_traveler))
print(test_destination_index)