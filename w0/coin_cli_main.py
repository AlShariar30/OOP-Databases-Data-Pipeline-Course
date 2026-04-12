from coin_acceptor import CoinAcceptor

print("Program starting.")
print("Welcome to coin acceptor program.")
print("Insert new coin by typing it's value (0 returns the money, -1 exits the program)")

coin_acceptor = CoinAcceptor()

while True:
    coin = float(input("Insert coin(0 return, -1 exit): "))

    if coin == -1:
        print("Exiting program.")
        print("Program ending.")
        break

    elif coin == 0:
        print("Returning coins...")
        amount, value = coin_acceptor.returnCoins()
        print(f"{amount} coins with {value}€ value returned.")
        print(f"Inserted coins = {coin_acceptor.getAmount()}, value = {coin_acceptor.getValue()}€")

    else:
        print("Inserting...")
        coin_acceptor.insertCoin(coin)
        print(f"Inserted coins = {coin_acceptor.getAmount()}, value = {coin_acceptor.getValue()}€")