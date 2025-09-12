Pattern = "IIIDIDDD"


def IncreaseDecrease(Pattern:list[str], Result:list[int] = [], idx:int = 0, DondeEstoy = 0, Seen = set() ) -> list[int]:
    if idx == 0:
        for _ in range(len(Pattern)):
            DondeEstoy = len(Pattern)
            Result.append(1)
  
    if idx == len(Pattern):
        return Result


    for i in range(DondeEstoy):
        if not i != DondeEstoy - 1:
            break
        if Pattern[i] == "I":
            Result[i + 1] = Result[i] + 1
            Seen.add(Result[i] + 1)
        else:
            Result[i + 1] = Result[i] - 1
            Seen.add(Result[i] - 1)


        



    return Result


print(IncreaseDecrease(Pattern))