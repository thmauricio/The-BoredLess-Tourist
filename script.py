destinations = ["Paris, France", "Shanghai, China",
                "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


def get_destination_index(destination):
    """This function takes as parameter a destination and returns the index of that destination in the destinations list"""
    return destinations.index(destination)
traveller_destination = test_traveler[1]

index = get_destination_index('Hyderabad, India')
print(index)