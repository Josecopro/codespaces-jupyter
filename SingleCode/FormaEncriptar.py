import string

alfabeto = list(string.ascii_lowercase)

    

print(alfabeto)


def Decode(n:int, s:str , strings:list = [], idx = 0) -> int:
    if n <= 0:
        strings.append(s[n:+idx])
        return 0
    if s[n:n+idx].isdigit() and int(s[n:n+2]) <= 26:
        strings.append(s[n:n+idx])
    Decode(n-1,s, strings, 1)
    Decode(n-2,s, strings, 2)
    print(strings)
    dictionary = {}
    for i, string in enumerate(strings):
        if string == "" or string[0] == "0":
            continue
        if string not in dictionary and int(string) < 27:
            dictionary[alfabeto[int(string) - 1]] = string
    return dictionary


print(Decode(2,"27"))

