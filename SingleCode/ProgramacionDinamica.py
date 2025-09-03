def Escaleras(n:int, TotalResult:int = 0, MemoDict = {}) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1
    
    if n not in MemoDict:
        MemoDict[n] = 1
        TotalResult += Escaleras(n-1, TotalResult, MemoDict) + Escaleras(n-2, TotalResult, MemoDict)
    else:
        MemoDict[n] += 1

    print(MemoDict)
    return TotalResult


print(Escaleras(7))
