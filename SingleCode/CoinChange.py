def CoinChange(Coins:list[int], Amount:list[int], idx:int, CoinCounter:list = []):    

    if idx < 0:
        return len(CoinCounter)

    if Coins[idx] <= Amount[0]:
        Amount[0] -= Coins[idx]
        CoinCounter.append(Coins[idx])
        CoinChange(Coins, Amount, idx, CoinCounter)
    else:
        idx -= 1
        CoinChange(Coins, Amount, idx, CoinCounter)

    if Amount[0] == 0:
        return len(CoinCounter)
    return -1
    

from typing import Dict

def MemoChange(n: int, Coins:list[int]) -> int:
    # caché inicial con los casos base
    memo: Dict[int, int] = {0: 0}  # 0 coins needed to make amount 0

    def dp(Amount: int, Coins:list[int]) -> int:
        if Amount in memo:
            return memo[Amount]

        if Amount < 0:
            return float('inf')
        
        MinCoins = float('inf')
        for coin in Coins:
            result = dp(Amount - coin, Coins)
            MinCoins = min(MinCoins, result + 1)
        
        memo[Amount] = MinCoins
        return memo[Amount]

    result = dp(n, Coins)
    return result if result != float('inf') else -1


print(MemoChange(5, [1,2,3]))



#print(CoinChange([1, 3], [3], 1 ))


    

    
