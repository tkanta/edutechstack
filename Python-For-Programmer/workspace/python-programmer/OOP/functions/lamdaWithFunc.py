def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator(operation, n1, n2):
    return operation(n1, n2)  # Using the 'operation' argument as a function


# result = calculator(multiply, 10, 20)
# print(result)
# print(calculator(add, 10, 20))

# 10 and 20 are the arguments.
result = calculator(lambda n1, n2: n1 * n2, 10, 20)
# The lambda multiplies them.
print(result)

print(calculator(lambda n1, n2: n1 + n2, 10, 20))

print(calculator(lambda n1, n2: n1 - n2, 220, 20))

# map() function with lambda
num_list = [1, 2, 3, 4, 5]
double_list = list(map(lambda n: 2 * n, num_list))
print(double_list)

# filter() func with lambda
gr_thn_1_list = list(filter(lambda n: n > 1, num_list))
print(gr_thn_1_list)
