class Complex:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        temp = Complex(self.real + other.real, self.imaginary + other.imaginary)
        return temp

    def __sub__(self, other):
        temp = Complex(self.real - other.real, self.imaginary - other.imaginary)
        return temp


comp1 = Complex(2, 3)
comp2 = Complex(4, 5)
comp3 = comp1 + comp2
comp4 = comp1 - comp2

print("real :", comp3.real)
print("imaginary :", comp3.imaginary)
print("real :", comp4.real)
print("imaginary :", comp4.imaginary)

