lista = ["a", "b", "c", "d", "e"]
r = 2
def combinaciones(lista: list[str], r, idx = 0, rpta:list[str] = [], rptatotal = []):
    if len(rpta) == r: 

        
        rptatotal.append(rpta[:])
        return 

    for i  in range(idx, len(lista)): #[1,2,3]
        rpta.append(lista[i])
        combinaciones(lista,r,i + 1, rpta, rptatotal)
        rpta.pop()
    return rptatotal


print(combinaciones(lista, r))