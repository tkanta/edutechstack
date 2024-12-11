class User:
    def __init__(self, name):
        self.__username = name
        self.name = name

    def getusername(self):
        return self.__username

    def setusername(self, name):
        self.__username = name


tarini = User("Tarini")
print(tarini.getusername())
tarini.setusername('Tarini Kanta')
print(tarini.getusername())
# Access private property
print(tarini.__username)
print(tarini.name)
