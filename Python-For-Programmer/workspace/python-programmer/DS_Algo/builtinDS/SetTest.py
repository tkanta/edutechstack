random_set = {"Educative", 1408, 3.142,
              (True, False)}
print(random_set)
print(len(random_set))

print(" -------- using set() -----------")

empty_set = set()
print(empty_set)

random_set = set({"Educative", 1408, 3.142, (True, False)})
print(random_set)

print(" -------- Creating lists, sets, tuples, and dictionaries -----------")

test_set = {"Educative", 1408, 3.142, (True, False)}
test_lst = ["Educative", 1408, 3.142, (True, False)]
test_dic = {1: "Educative", 2: 1408, 3: 3.142, 4: (True, False)}
test_tup = ("Educative", 1408, 3.142, (True, False))

print(type(test_set))
print(type(test_lst))
print(type(test_dic))
print(type(test_tup))

print(" -------- Adding elements -----------")

empty_set = {50}
print(empty_set)

empty_set.add(1)
print(empty_set)

empty_set.update([2, 2, 3, 4, 5, 5, 5, 6])
print(empty_set)