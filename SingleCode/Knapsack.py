from typing import Dict

n = 3
W = 50
pesos = [10, 20, 30]
valores = [60, 100, 120]




def KnapsackMemo(NItems: int, TotalWeight: int, Weights: list[int], Values: list[int]) -> int:
    # Memoization dictionary: key = (current_item_index, remaining_weight)
    memo: Dict[tuple, int] = {}

    def dp(item_idx: int, remaining_weight: int) -> int:
        # Base case: no more items or no remaining weight
        if item_idx >= NItems or remaining_weight <= 0:
            return 0
        # Check if already computed
        if (item_idx, remaining_weight) in memo:
            return memo[(item_idx, remaining_weight)]
        
        # Option 1: Don't take the current item
        max_value = dp(item_idx + 1, remaining_weight)
        
        # Option 2: Take the current item (if it fits)
        if Weights[item_idx] <= remaining_weight:
            take_value = Values[item_idx] + dp(item_idx + 1, remaining_weight - Weights[item_idx])
            max_value = max(max_value, take_value)
        
        # Memoize and return
        memo[(item_idx, remaining_weight)] = max_value
        return max_value
    
    return dp(0, TotalWeight)

print(KnapsackMemo(n, W, pesos, valores))