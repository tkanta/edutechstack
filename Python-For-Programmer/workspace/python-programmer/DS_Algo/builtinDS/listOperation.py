houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", "Hufflepuff"]
last_house = houses.pop(2)
print(last_house)
print(houses.count("Hufflepuff"))

gardens = ["jublee", "ayyappa"]

combine = houses + gardens
houses.extend(gardens)
houses.append("test")
print(houses)