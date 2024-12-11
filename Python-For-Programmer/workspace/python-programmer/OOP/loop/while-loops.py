# Add first and last number
num = 249
last_no = num % 10

first_no = num
while first_no >= 10:
    first_no //= 10

result = first_no + last_no
print("sum of {first} and {last} no : {result} ".format(first=first_no, last=last_no, result=result))

# Find power of a number > 1000
n = 2
power = 0
val = n
while val < 1000:
    power += 1
    val *= n
    print(val)
print("power : ", power)
