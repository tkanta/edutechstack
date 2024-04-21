
print("----------- addition ------------")
num = 20
fltNo = 10.5
print("int + flt : ", num+fltNo)

print("----------- subtraction ------------")
num = -20
fltNo = 10.5
print("int - flt : ", num-fltNo)

print("----------- Multiplication ------------")
print("flt * int : ", 10.2 * 3)

print("----------- division ------------")
print("flt / int : ", 15.8 / 2)

print("----------- floor division ------------")
print("flt // int : ", 15.8 // 2)

print(10 % 2)

print("----------- modulo ------------")
twenty_eight = 28
print("28 % 10 : ", twenty_eight % 10)

print("-3 % 8 : ", -3 % 8)  # The remainder is positive if the right-hand operand is positive
print("28 % -10 : ", 28 % -10)  # The remainder is negative if the right-hand operand is negative
print(34.4 % 2.5)  # The remainder can be a float

print("----------- comparison operator ------------")
num1 = 5
num2 = 10.8
num3 = 10.8
list1 = [6,7,8]
list2 = [6,7,8]
list3 = list1

print(num2 > num1)  # 10 is greater than 5
print(num1 > num2)  # 5 is not greater than 10

print(num2 == num3)  # Both have the same value
print(num3 != num1)  # Both have different values

print(3 + 10 == 5 + 5)  # Both are not equal
print(3 <= 2)  # 3 is not less than or equal to 2

print(num2 is num3)  # Both have the same object
print(list1 is not list3)  # Both have the different objects

print("------------- variable assignment ---------------")
first = 20
second = first
first = 35  # Updating 'first'
print(first, second)  # 'second' remains unchanged

print("------------- logical operator ---------------")
print(10 * True)
print(10 * False)

print("---------- bitwise operator -------------------")
num1 = 10  # Binary value = 01010
num2 = 20  # Binary Value = 10100

print(num1 & num2)   # 0   -> Binary value = 00000
print(num1 | num2)   # 30  -> Binary value = 11110
print(num1 ^ num2)   # 30  -> Binary value = 11110
print(~num1)         # -11 -> Binary value = -(1011)
print(num1 << 3)     # 80  -> Binary value = 0101 0000
print(num2 >> 3)     # 2   -> Binary value = 0010

print("---------- string operation  -------------------")
print('random' in 'random_exist')
print("ha" * 3)

print(2 + True)

print("--------------- gravitational force ---------------")

G = 6.67 * (10 ** -11)
M = 6.0 * (10 ** 24)
m = 7.34 * (10 ** 22)
r = 3.84 * (10 ** 8)

fg = (G*M*m)/(r ** 2)
print ("grav_force : ", fg)