from wallet import CryptoWallet

wallets = []

while True:
    print("\nMenu:")
    print("1 - Create Wallet")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Check Balance")
    print("5 - Transaction History")
    print("0 - Exit")

    choice = input("Choice: ")

    if choice == "1":
        walletId = input("Enter wallet ID: ")
        wallet = CryptoWallet(walletId)
        wallets.append(wallet)
        print("Wallet created.")

    elif choice in ["2", "3", "4", "5"]:
        if len(wallets) == 0:
            print("No wallets available.")
            continue

        index = int(input("Select wallet index (starting from 0): "))
        if index < 0 or index >= len(wallets):
            print("Invalid wallet index.")
            continue

        wallet = wallets[index]

        if choice == "2":
            amount = float(input("Enter deposit amount: "))
            wallet.deposit(amount)

        elif choice == "3":
            amount = float(input("Enter withdraw amount: "))
            wallet.withdraw(amount)

        elif choice == "4":
            print(f"Balance: {wallet.getBalance()}")

        elif choice == "5":
            history = wallet.getTransactionHistory()
            if len(history) == 0:
                print("No transactions yet.")
            else:
                for h in history:
                    print(h)

    elif choice == "0":
        print("Program ending.")
        break

    else:
        print("Invalid menu choice.")