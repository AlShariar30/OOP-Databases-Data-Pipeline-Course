from abc import ABC, abstractmethod


class GameCharacter(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass


class Warrior(GameCharacter):
    def attack(self):
        print(f"{self.name} swings a sword!")

    def defend(self):
        print(f"{self.name} blocks with a shield!")


class Mage(GameCharacter):
    def attack(self):
        print(f"{self.name} casts a fireball!")

    def defend(self):
        print(f"{self.name} uses a magic barrier!")


class Archer(GameCharacter):
    def attack(self):
        print(f"{self.name} shoots an arrow!")

    def defend(self):
        print(f"{self.name} dodges quickly!")