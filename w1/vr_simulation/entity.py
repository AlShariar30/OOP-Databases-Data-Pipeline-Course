class Entity:
    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position

    def interact(self):
        print(f"{self.name} interacts at {self.position}.")


class Player(Entity):
    def __init__(self, name: str, position: str, level: int):
        super().__init__(name, position)
        self.level = level

    def interact(self):
        print(f"Player {self.name} at {self.position} explores the world at level {self.level}.")


class NPC(Entity):
    def __init__(self, name: str, position: str, role: str):
        super().__init__(name, position)
        self.role = role

    def interact(self):
        print(f"NPC {self.name} at {self.position} gives a {self.role} interaction.")


class Object(Entity):
    def __init__(self, name: str, position: str, object_type: str):
        super().__init__(name, position)
        self.object_type = object_type

    def interact(self):
        print(f"Object {self.name} at {self.position} behaves like a {self.object_type}.")