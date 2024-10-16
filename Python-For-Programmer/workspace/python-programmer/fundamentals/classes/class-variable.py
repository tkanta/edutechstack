class Player:
    teamName = 'LiverPool'
    teamMembers = []

    def __init__(self, name):
        self.name = name
        self.teamMembers.append(name)


player1 = Player("Tarun")
player2 = Player("Itu")
player2 = Player("Rattan")

print(player1.name)
print(player1.teamName)
print(player1.teamMembers)
print(player2.name)
print(player2.teamName)
print(player2.teamMembers)
