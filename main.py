import random


# exercise 2
class Collectables:
    total_points = 0

    def __init__(self, name):
        self.name = name
        self.value = 9

    def collect(self):
        Collectables.total_points = + self.value


class Potions(Collectables):
    colours = ["red", "blue", "green", "yellow"]

    def __init__(self, name, value):
        Collectables.__init__(self, name)
        self.value = value
        self.colours = random.choice(Potions.colours)


class Coins(Collectables):

    def __init__(self, name, value):
        Collectables.__init__(self, name)
        self.value = value
    pass

collectable = Collectables
coin = Coins("coin", 1)
potion = Potions("potion", 2)

print(vars(coin))
print(vars(potion))
print()

while Collectables.total_points < 300:
    choice = input("Enter a number between 1 and 6 ")
    if not choice.isdigit():
        print("Not a number")
        break

    if choice.int() > 6:
        print("Too high")
        break

    if choice.int() <= 3:
        coin = Coins


# exercise 1
class Enemy:

    weapon_list = {"knife": 5, "sword": 10, "bat": 15}
    name_list = ["Steve", "Stan", "Kieth", "Edwin", "Ben"]
    homelands = ["Uxbridge", "River", "Riverdale", "Gaskell"]
    abilities = ["Blizzard", "Seduce", "Annoy", "Gaslight"]

    def __init__(self, name, homeland, ability):

        self.name = name
        self.homeland = homeland
        self.ability = ability

    def set_bio(self, bio):
        if not isinstance(bio, str):
            print("Bio must be a string.")
            return
        self.bio = bio

    def get_bio(self):
        return self.bio

    def get_random_weapon(self):

        self.weapon = random.choice(list(Enemy.weapon_list.items()))

print()
enemy1 = Enemy("Stan", "Devon", "Enrage")
enemy1.set_bio("Cool Enemy")
enemy1.get_random_weapon()
print(vars(enemy1))
enemy2 = Enemy("Dog", "River", "Drunken Master")
enemy2.set_bio("Other Enemy")
enemy2.get_random_weapon()
print(vars(enemy2))


for i in range(4):
    name = Enemy.name_list[i]
    homeland = random.choice(Enemy.homelands)
    ability = random.choice(Enemy.abilities)
    enemy = Enemy(name, homeland, ability)
    enemy.set_bio("{} is from {} and their ability is {}.".format(name, enemy.homeland, enemy.ability))

print()
print(enemy.get_bio())
