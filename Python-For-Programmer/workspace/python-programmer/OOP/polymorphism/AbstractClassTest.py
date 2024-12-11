from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, length=0):
        self.length = length

    def area(self):
        return self.length * self.length


shape = Square(7)
print(shape.area())


# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):  # Shape is a child class of ABC
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#
# class Square(Shape):
#     def __init__(self, length):
#         self.length = length
#
#     def area(self):
#         return (self.length * self.length)
#
#     def perimeter(self):
#         return (4 * self.length)
#
#
# shape = Square(8)
# print(shape.area())
# # this code will not compile since Shape has abstract methods without
# # method definitions in it