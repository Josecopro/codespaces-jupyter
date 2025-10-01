s = "pineapplepenapple"
wordDict = ["apple","pen","applepen","pine","pineapple"]

def ValidWords(s:str, worddict:list[str], result:str = "", actualWord:str = "", totalresult:list[list[str]] = [], idx: int = 0):
    if  s == "":
        print("a")
        totalresult.append(result[:-1])
        return totalresult
    

    for i  in range(len(s)):
        actualWord += s[i]
        if actualWord in worddict:
            ValidWords(s[i + 1:],wordDict, result + actualWord + " ", "", totalresult, i)

    return totalresult


print(ValidWords(s, wordDict))

