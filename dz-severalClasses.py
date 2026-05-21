class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.inv = []
    def attack(self, enemy):
        enemy.hp -= self.damage
        print(self.name, "атакує", enemy.name)
    def add_it(self, item):
        self.inv.append(item)
    def show_inv(self):
        print("Інвентар:")
        for i in self.inv:
            print(i.name, "-", i.value)

class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def attack(self, player):
        player.hp -= self.damage
        print(self.name, "атакує", player.name)

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

player = Player("Леон", 100, 20)
enemy = Enemy("Краузер", 60, 10)
bow = Item("Bow", 90)
potion = Item("Potion", 30)
player.add_it(bow)
player.add_it(potion)
player.show_inv()

print("START")
while player.hp > 0 and enemy.hp > 0:
     player.attack(enemy)
     print(enemy.name, "HP:", enemy.hp)
     enemy.attack(player)
     print(player.name, "HP:", player.hp)
     if player.hp > 0:
         print("Леон виграв!")
     else:
         print("Краузер виграв!")

print("END")