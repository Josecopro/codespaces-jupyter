def GriddyCoinChange(Coins:list[int], Target: int):
    numCoins = 0 
    while Target > 0:
        if Target - max(Coins) >= 0:
            Target -= max(Coins)
            numCoins += 1
        else:
            Coins.pop()
    return numCoins

print(GriddyCoinChange([1,3,4], 6))