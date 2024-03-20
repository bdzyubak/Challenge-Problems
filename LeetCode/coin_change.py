def coinChange(coins, amount):
    coins.sort()
    n = 0
    ind_coin = -1
    while amount and ind_coin >= -len(coins):
        how_many = amount // coins[ind_coin]
        if how_many:
            n += how_many
        amount = amount % coins[ind_coin]
        print(f"{amount} {ind_coin} {how_many}")
        ind_coin -= 1

    if amount == 0:
        return n
    else:
        return -1


coins = [1, 5, 10, 25]
amount = 68
assert coinChange(coins, amount) == 7

coins = [1, 7, 8]
amount = 21
assert coinChange(coins, amount) == 3

coins = [186, 419, 83, 408]
amount = 6249
assert coinChange(coins, amount) == 20
