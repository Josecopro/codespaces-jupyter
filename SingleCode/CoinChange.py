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
    memo: Dict[int, int] = {0: 1}

    def dp(Amount: int, Coins:list[int], idx:int = 0, listica:list[int] =[]) -> int:
        if Amount == 0:
            listica.append(idx)
        if Amount in memo:

            return memo[Amount]

        if Amount < 0:
            return 0
        
        for coin in Coins:
            if Amount in memo.keys():
                memo[Amount] += dp(Amount - coin, Coins, idx + 1)
            else:
                memo[Amount] = dp(Amount - coin, Coins, idx + 1)
        print(memo)
        print(listica)
        return memo[Amount]

    return dp(n, Coins)


print(MemoChange(6, [1,2,3]))



#print(CoinChange([1, 3], [3], 1 ))


    

    
