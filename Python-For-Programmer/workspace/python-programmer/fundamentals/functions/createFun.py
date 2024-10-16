def my_print_func():
    print("Test print....")


def minimum(first, second):
    if first < second:
        return first
    return second


num_list = [10, 20, 30, 40]
print(num_list)


def multiply_by_10(my_list):
    my_list[0] *= 10
    my_list[1] *= 10
    my_list[2] *= 10
    my_list[3] *= 10


my_print_func()
print("small number : ", minimum(110, 320))
multiply_by_10(num_list)
print(num_list)

# join list
llist = ['a', 'b', 'c']
print('>>'.join(llist))  # joining strings with >>
print('<<'.join(llist))  # joining strings with <<
print(', '.join(llist))  # joining strings with comma and space

# Format string
string1 = "Learn Python {version} at {cname}".format(version=3, cname="Educative")
string2 = "Learn Python {0} at {1}".format(3, "Educative")
string3 = "Learn Python {} at {}".format(3, "Educative")

print(string1)
print(string2)
print(string3)

my_func = lambda num: "High" if num > 50 else "Low"
triple = lambda num: num * 3
print(my_func(70))
print(triple(70))
