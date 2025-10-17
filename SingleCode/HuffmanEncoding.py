s = "AAABABBCaGSGAV"

class Node:
    def __init__(self, Value:tuple[int,str]=None, left=None, right=None):
        self.Value= Value
        self.left = left
        self.right = right



    

def HuffmanEncoding(s:str,Frecuencies = None, ActualNode:Node = None):

    def ContarYOrdenar(string, Diccionario:dict = {}):
        for char in string:
            if char in Diccionario:
                Diccionario[char] += 1
            else:
                Diccionario[char] = 1
        return sorted(Diccionario.items(),key = lambda x: x[1])
            

    if not Frecuencies:
        Frecuencies = ContarYOrdenar(s)

    for i in range(len(Frecuencies)):
        if len(Frecuencies) >= 2:
            valor = Frecuencies[i][1] + Frecuencies[i + 1][1]
            ActualNode = Node(Value = valor, left= Frecuencies[i], right=Frecuencies[i+ 1])
            Frecuencies.remove(Frecuencies[i])
            Frecuencies.remove(Frecuencies[i + 1])
        else:
            valor = Frecuencies[i][1]
            ActualNode = Node(Value= valor, left = Frecuencies[i])
            Frecuencies.remove(Frecuencies[i])
        
        Frecuencies.append(ActualNode)


    

    

    return ActualNode


print(HuffmanEncoding(s))