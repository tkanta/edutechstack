class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def total(self):
        return self.phy + self.chem + self.bio

    def percentage(self):
        return (self.total() / 300) * 100


student = Student("Tarini", 40, 50, 80)

print(F'Percentage Of {student.name} : {student.percentage()} %')

print("Percentage of {} :  {:.2f} %".format(student.name, student.percentage()))

print("Percentage of {} :  {:5%}".format(student.name, student.percentage()))
