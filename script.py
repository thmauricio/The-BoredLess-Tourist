def get_destination_index(destination):
    """This function takes as parameter a destination and returns the index of that destination in the destinations list"""
    return destinations.index(destination)


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

def find_attractions(destination, interests):
    """This function takes as parameters a destination and a list of interests and returns a list of attractions"""
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attraction_with_interest = []
    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = attraction[1]
        for interest in interests:
            if interest in attraction_tags:
                attraction_with_interest.append(possible_attraction[0])
    return attraction_with_interest

destinations = ["Paris, France", "Shanghai, China",
                "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]       

attractions = [[] for destination in destinations]

add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
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

la_arts = find_attractions("Los Angeles, USA", ["art"])

print(la_arts)

