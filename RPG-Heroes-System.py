class Character:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp
        self.inventory = []
    def info(self):
        print("Ім'я:", self.name)
        print("Рівень:", self.level)
        print("HP:", self.hp)
    def rest(self):
        self.hp += 10
        print(self.name, "відпочиває")
    def attack(self, target):
        damage = 5
        target.hp -= damage
        print(self.name, "атакує", target.name, "на", damage)

class Warrior(Character):
    def __init__(self, name, level, hp, shield):
        super().__init__(name, level, hp)
        self.shield = shield
    def attack(self, target):
        damage = 15 + self.shield
        target.hp -= damage
        print(self.name, "б'є мечем на", damage)
    def block(self):
        print(self.name, "блокує удар")

class Mage(Character):
    def __init__(self, name, level, hp, mana):
        super().__init__(name, level, hp)
        self.mana = mana
    def attack(self, target):
        if self.mana >= 10:
            damage = 20
            target.hp -= damage
            self.mana -= 10
            print(self.name, "кастує магію на", damage)
        else:
            print(self.name, "немає мани")

class Archer(Character):
    def __init__(self, name, level, hp, energy):
        super().__init__(name, level, hp)
        self.energy = energy
    def attack(self, target):
        if self.energy >= 5:
            damage = 12
            target.hp -= damage
            self.energy -= 5
            print(self.name, "стріляє на", damage)
        else:
            print(self.name, "немає енергії")

warrior = Warrior("Леон", 5, 120, 10)
mage = Mage("Карлос", 5, 80, 30)
archer = Archer("Ітан", 5, 90, 20)
players = [warrior, mage, archer]

print("INFO")
for p in players:
    p.info()

enemy = Character("Монстр", 1, 150)

print("BATTLE")
for p in players:
    p.attack(enemy)
    print("HP ворога:", enemy.hp)

print("END")
enemy.info()