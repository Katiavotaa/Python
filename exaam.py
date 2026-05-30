class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level
    def attack(self):
        print(self.name, "атакує")
    def defend(self):
        print(self.name, "захищається")
    def status(self):
        print("Ім'я:", self.name)
        print("HP:", self.hp)
        print("Рівень:", self.level)

class Warrior(Character):
    def attack(self):
        print(self.name, "б'є мечем")
    def defend(self):
        print(self.name, "блокує щитом")

class Mage(Character):
    def attack(self):
        print(self.name, "використовує магію")
    def defend(self):
        print(self.name, "створює щит")

class Scout(Character):
    def attack(self):
        print(self.name, "стріляє з лука")
    def defend(self):
        print(self.name, "ухиляється")

class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members
    def total_power(self):
        power = 0
        for member in self.members:
            power = power + member.level
        print("Сила команди:", power)
    def find_strongest(self):
        strongest = self.members[0]
        for member in self.members:
            if member.level > strongest.level:
                strongest = member
        print("Найсильніший:", strongest.name)

class Arena:
    def battle(self, fighter1, fighter2):
        print("БІЙ ПОЧАВСЯ")
        print("Раунд 1")
        damage1 = fighter1.level * 2
        fighter2.hp = fighter2.hp - damage1
        print(fighter1.name, "атакує і наносить", damage1, "урону")
        fighter2.attack()
        fighter1.defend()
        print()
        print("Раунд 2")
        damage2 = fighter2.level * 2
        fighter1.hp = fighter1.hp - damage2
        print(fighter2.name, "атакує і наносить", damage2, "урону")
        fighter1.attack()
        fighter2.defend()
        print()
        print("ФІНАЛ")
        print(fighter1.name, "HP:", fighter1.hp)
        print(fighter2.name, "HP:", fighter2.hp)
        if fighter1.hp > fighter2.hp:
            print("Переможець:", fighter1.name)
        elif fighter2.hp > fighter1.hp:
            print("Переможець:", fighter2.name)
        else:
            print("Нічия")

warrior = Warrior("Леон", 100, 5)
mage = Mage("Геральд", 80, 6)
scout = Scout("Вернон", 90, 4)
team = Team("Alpha", [warrior, mage, scout])
print()
warrior.status()
print()
mage.status()
print()
scout.status()
print()
team.total_power()
team.find_strongest()
print()
print("Вибір бійців:")
print("1 - Леон")
print("2 - Геральд")
print("3 - Вернон")

choice1 = input("Перший боєць: ")
choice2 = input("Другий боєць: ")
if choice1 == "1":
    fighter1 = warrior
elif choice1 == "2":
    fighter1 = mage
else:
    fighter1 = scout

if choice2 == "1":
    fighter2 = warrior
elif choice2 == "2":
    fighter2 = mage
else:
    fighter2 = scout

arena = Arena()
arena.battle(fighter1, fighter2)