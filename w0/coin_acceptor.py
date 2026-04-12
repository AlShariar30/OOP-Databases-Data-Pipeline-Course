class CoinAcceptor:
    def __init__(self):
        self.__amount = 0
        self.__value = 0.0

    def insertCoin(self, coin: float):
        self.__amount += 1
        self.__value += coin

    def getAmount(self):
        return self.__amount

    def getValue(self):
        return self.__value

    def returnCoins(self):
        coins = self.__amount
        value = self.__value
        self.__amount = 0
        self.__value = 0.0
        return coins, value