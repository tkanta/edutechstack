# Creating an empty dictionary
empty_dict = {}
print(empty_dict)

# Creating a phone book using a dictionary
phone_book = {
    'Alice': 1234567890,
    'Bob': 9876543210,
    'Charlie': 'unknown',
    123: 5555555.55
}

# Printing the phone book
print(phone_book)
print(phone_book.get(123))

# ------------------------------------------

empty_dict = dict()  # Empty dictionary
print(empty_dict)

phone_book = dict(Batman=468426, Cersei=237734, Ghostbusters=44678)
# Keys will automatically be converted to strings
print(phone_book)

# Alternative approach
phone_book = dict([('Batman', 468426),
                   ('Cersei', 237734),
                   ('Ghostbusters', 44678)])
print(phone_book.get("Batman"))

print(" ------------- dictionary comprehension --------- ")

houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n * 2: house + "!" for (n, house) in houses.items() if house != "Hufflepuff"}
print(houses)
print(new_houses)

squares = {1: 1, 2: 4, 3: 9, 4: 16}
new_squares = {k * 2: v + 1 for (k, v) in squares.items()}  # Your code here
print(new_squares)
