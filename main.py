from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом")

class Bow(Weapon):
    def attack(self):
        print("Боец стреляет из лука")

class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает новое оружие.")

    def fight(self):
        print(f"{self.name} наносит удар ")
        self.weapon.attack()


class Monster:
    def __init__(self, name):
        self.name = name

    def defeat(self):
        print(f"{self.name} побежден!")


    # Создаем оружие
sword1 = Sword()
bow1 = Bow()

    # Создаем бойца и монстра
fighter = Fighter("Боец", sword1)
monster = Monster("Монстр")



    # Боец выбирает лук и атакует монстра
fighter.change_weapon(bow1)
fighter.fight()
monster.defeat()

    # Боец выбирает меч и атакует монстра
fighter.change_weapon(sword1)
fighter.fight()
monster.defeat()


