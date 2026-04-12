class CryptoWallet:
    def __init__(self, walletId: str):
        self.__walletId = walletId
        self.__balance = 0.0
        self.__transactions = []

    def deposit(self, amount: float):
        if amount <= 0:
            print("Invalid deposit amount.")
            return
        self.__balance += amount
        self.__transactions.append(f"Deposited {amount}")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Invalid withdraw amount.")
            return
        if amount > self.__balance:
            print("Insufficient balance.")
            return
        self.__balance -= amount
        self.__transactions.append(f"Withdrew {amount}")

    def getBalance(self):
        return self.__balance

    def getTransactionHistory(self):
        return self.__transactions