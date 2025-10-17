

def RemoveLetters(s:str):
    res:list = []
    FrequencyList = dict()
    for element in s:
        if element in FrequencyList:
            FrequencyList[element] += 1
        else:
            FrequencyList[element] = 1

    for i in range(len(s)):
        if i == 0:
            res.append(i)
        elif s[i] < s[i - 1]:
            pass


    return FrequencyList

s = "cbdbcabc"

print(RemoveLetters(s))




        