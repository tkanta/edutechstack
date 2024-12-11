
# index function with list comprehension

cities_set1 = ("London", "Paris", "Los Angeles", "Tokyo")
print(cities_set1.index("Tokyo"))


cities_set2 = (
    ("London", 8.9, "UK"),
    ("Paris", 2.1, "France"),
    ("Los Angeles", 3.9, "USA"),
    ("Tokyo", 14.0, "Japan")
)

# index of city is the index of the tuple in the tuple list
tokyo_index = [city[0] for city in cities_set2].index("Tokyo")
city_names = [city[0] for city in cities_set2]
print(f"Index of Tokyo: {tokyo_index}")
print(city_names)

print(cities_set1)