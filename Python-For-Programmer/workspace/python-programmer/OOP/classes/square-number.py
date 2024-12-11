class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sq_sum(self):
        a = self.x * self.x
        b = self.y * self.y
        c = self.z * self.z
        return a + b + c


point = Point(2, 2, 2)
print("sum of 2, 2, 2 : ", point.sq_sum())
