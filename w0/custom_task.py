class BankAccount:
    def __init__(self):
        self.__balance = 0.0

    def deposit(self, amount: float):
        self.__balance += amount

    def withdraw(self, amount: float):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def getBalance(self):
        return self.__balance


print("Program starting.")
print("Initializing bank account...")

account = BankAccount()

print("Bank account initialized.")

while True:
    print("\nOptions:")
    print("1) Deposit money")
    print("2) Withdraw money")
    print("3) Show balance")
    print("0) Exit program")

    choice = input("Choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
        print(f"Deposited {amount}")

    elif choice == "2":
        amount = float(input("Enter withdraw amount: "))
        if account.withdraw(amount):
            print(f"Withdrew {amount}")
        else:
            print("Not enough balance")

    elif choice == "3":
        print(f"Current balance: {account.getBalance()}")

    elif choice == "0":
        print("Program ending.")
        break

    else:
        print("Invalid choice")