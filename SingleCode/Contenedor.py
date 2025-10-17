def Contenedor(Heights:list, Max:tuple[int,int] = (0,0), ScndMax:tuple[int,int] = (0,0)):
    

    for i  in range(len(Heights)):
        
        if Heights[i] > Max[0]:
            ScndMax = Max
            Max = (i,Heights[i])
        
    return abs(Max[0]  - ScndMax[0] * Max[1] - ScndMax[1])



height = [1,8,6,2,5,4,8,3,7]

print(Contenedor(height))
        
