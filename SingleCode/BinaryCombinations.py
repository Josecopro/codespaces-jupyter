n = 3

def BinaryCombinations(n:int,idx = 0, PartialResult:str = "" ,Result:list[str] = []):
    if idx == n:
        if PartialResult != "000":
            Result.append(PartialResult)
        return Result
        
    for Element in ["0","1"]:
        BinaryCombinations(n, idx + 1, PartialResult + Element, Result)

    return Result


print(BinaryCombinations(n))
    