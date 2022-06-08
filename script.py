destinations = ["Paris, France", "Shanghai, China",
                "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


def get_destination_index(destination):
    """This function takes as parameter a destination and returns the index of that destination in the destinations list"""
    index = 0
    for local in destinations:
        if destination == local:
            return index
            break
        index += 1

traveller_destination = test_traveler[1]

index = get_destination_index(traveller_destination)
print(index)