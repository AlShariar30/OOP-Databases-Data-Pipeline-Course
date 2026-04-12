from character import Warrior, Mage, Archer


def simulate_battle(characters):
    print("\nBattle starting...")
    for character in characters:
        character.attack()
        character.defend()
    print("Battle ended.")


characters = []

while True:
    print("\nMenu:")
    print("1 - Create Character")
    print("2 - Simulate Battle")
    print("0 - Exit")

    choice = input("Choice: ")

    if choice == "1":
        print("Choose character type:")
        print("1 - Warrior")
        print("2 - Mage")
        print("3 - Archer")

        char_choice = input("Character type: ")
        name = input("Enter character name: ")

        if char_choice == "1":
            character = Warrior(name)
        elif char_choice == "2":
            character = Mage(name)
        elif char_choice == "3":
            character = Archer(name)
        else:
            print("Invalid character choice.")
            continue

        characters.append(character)
        print("Character created successfully.")

    elif choice == "2":
        if len(characters) == 0:
            print("No characters created yet.")
        else:
            simulate_battle(characters)

    elif choice == "0":
        print("Program ending.")
        break

    else:
        print("Invalid menu choice.")