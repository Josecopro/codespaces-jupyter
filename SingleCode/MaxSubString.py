def MaxSubString(s:str, Ls:int = 0, Rs:int = 0):

    Total = 0

    for letters in s:
        if letters == "L":
            Ls += 1
        else:
            Rs += 1

        if Ls == Rs:
            Total += 1


    return Total


print(MaxSubString("LRLRLLLRRR"))

