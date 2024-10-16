class BodyInfo:
    variable = 10

    @staticmethod
    def bmi(weight, height):
        return weight / (height**2)


weight_1 = 75
height_1 = 1.8
print(BodyInfo.bmi(weight_1, height_1))