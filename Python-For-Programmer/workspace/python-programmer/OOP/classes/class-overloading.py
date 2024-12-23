class Employee:
    # defining the properties and assigning them None to the
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    # method overloading
    def demo(self, a, b, c, d=5, e=None):
        print("first")
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)

    def demo(self, a, b, c, d=3):
        print("second")
    def tax(self, title=None):
        return (self.salary * 0.2)

    def salaryPerDay(self):
        return (self.salary / 30)


# cerating an object of the Employee class
Steve = Employee()

# Printing properties of Steve
print("Demo 1")
Steve.demo(1, 2, 3)
print("\n")

print("Demo 2")
Steve.demo(1, 2, 3, 4)
print("\n")

print("Demo 3")
#Steve.demo(1, 2, 3, 4, 5)