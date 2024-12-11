class Rectangle:
    def __init__(self, length=0, width=0):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)


rectangle = Rectangle(2, 3)
print("Area :", rectangle.area())
print("perimeter : ", rectangle.perimeter())
