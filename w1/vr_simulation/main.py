from entity import Player, NPC, Object


def interact_with_entities(entities):
    print("\nInteracting with entities...")
    for entity in entities:
        entity.interact()


entities = []

while True:
    print("\nMenu:")
    print("1 - Add Entity")
    print("2 - Interact with Entities")
    print("3 - Exit")

    choice = input("Choice: ")

    if choice == "1":
        print("Choose entity type:")
        print("1 - Player")
        print("2 - NPC")
        print("3 - Object")

        entity_choice = input("Entity type: ")
        name = input("Enter name: ")
        position = input("Enter position: ")

        if entity_choice == "1":
            level = int(input("Enter level: "))
            entity = Player(name, position, level)
        elif entity_choice == "2":
            role = input("Enter NPC role: ")
            entity = NPC(name, position, role)
        elif entity_choice == "3":
            object_type = input("Enter object type: ")
            entity = Object(name, position, object_type)
        else:
            print("Invalid entity choice.")
            continue

        entities.append(entity)
        print("Entity added successfully.")

    elif choice == "2":
        if len(entities) == 0:
            print("No entities added yet.")
        else:
            interact_with_entities(entities)

    elif choice == "3":
        print("Program ending.")
        break

    else:
        print("Invalid menu choice.")