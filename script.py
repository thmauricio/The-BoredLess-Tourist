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

def add_attraction(destination, attraction):
    """This function takes as parameters a destination and an attraction"""
    try:
        destination_index = get_destination_index(destination)
        attraction_for_destination = attractions[destination_index].append(attraction)
    except ValueError:
        return
        

test_destination_index = get_destination_index(get_traveler_location(test_traveler))
print(test_destination_index)

attractions = [[] for destination in destinations]

add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
print(attractions)
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print(attractions)