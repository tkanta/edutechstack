print("------------- Comments ----------------------")
#print("Hello world")
"""
print(50, 1000, 3.142, "Hello World")
print("Hello", end="")
print("World")
"""
print("Hello", end=" ")
print("World")
print("Tarini", end=" ")
print("Kanta Negi")
print(True)

# Numbers
print("-------- Numbers ---------")
no = 30.5
print(no)

flt_pt = 1.23456789
print(flt_pt)
print(-85.6701)

complex_1 = complex(2, 0)
print(complex_1)
print(complex(10, .3))

# String
print("--------- Strings --------")
multiple_lines = '''Triple quotes allows
multi-line string.'''
print(multiple_lines)
print(len(multiple_lines))
print(multiple_lines[len(multiple_lines) - 1])

#string = "Immutability"
#string[0] = 'O' # Will give error

str1 = "hello"
print("hello string id - >", id(str1))

str1 = "test"
print("test string id - >", id(str1))

testStr = "Tarini Kanta Negi"
#print(testStr[::2])
print(testStr[len(testStr):1:-1])


