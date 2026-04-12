from coin_acceptor import CoinAcceptor

print("Program starting.")

coin_acceptor = CoinAcceptor()

while True:
    print("\n1 - Insert coin")
    print("2 - Show coins")
    print("3 - Return coins")
    print("0 - Exit program")

    choice = input("Your choice: ")

    if choice == "1":
        coin_acceptor.insertCoin()

    elif choice == "2":
        print(f"Currently '{coin_acceptor.getAmount()}' coins in coin acceptor")

    elif choice == "3":
        coins = coin_acceptor.returnCoins()
        print(f"Coin acceptor returned '{coins}' coins.")

    elif choice == "0":
        print("Program ending.")
        break

    else:
        print("Invalid choice")