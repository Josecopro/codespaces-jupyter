matriz = []
Filas =[7, 22, 16]
Columnas = [16, 13, 16]
n = 3
for i in range(n):
    matriz.append([])
    for j in range(n):
        matriz[i].append(0)    

result = []

def VerifySum(matriz, ResultadoFilas, ResultadoColumnas):
    n = len(matriz)
    
    for i in range(n):
        suma_fila = sum(matriz[i])
        if suma_fila != ResultadoFilas[i]:
            return False
    
    for j in range(n):
        suma_columna = sum(matriz[i][j] for i in range(n))
        if suma_columna != ResultadoColumnas[j]:
            return False
    
    return True

def Juego(matriz, ResultadoFilas, ResultadoColumnas, fila=0, col=0, elementos = []):
    n = len(matriz)
    
    if fila == n:
        if VerifySum(matriz, ResultadoFilas, ResultadoColumnas):
            solucion = [fila[:] for fila in matriz]
            result.append(solucion)
            return True
        return False
    
    SiguienteFila = fila
    SiguienteCol = col + 1
    if SiguienteCol == n:
        SiguienteFila += 1
        SiguienteCol = 0
    
    for valor in range(1, len(matriz) ** 2 + 1): 
        if valor in elementos:
            continue

        matriz[fila][col] = valor
        elementos.append(valor)
        CanWork = True
        
        if col == n - 1:
            SumFila = sum(matriz[fila])
            if SumFila != ResultadoFilas[fila]:
                CanWork = False
        
        if fila == n - 1:
            SumColumna = sum(matriz[i][col] for i in range(n))
            if SumColumna != ResultadoColumnas[col]:
                CanWork = False
        
        if CanWork:
            if Juego(matriz, ResultadoFilas, ResultadoColumnas, SiguienteFila, SiguienteCol):
                return True  
        matriz[fila][col] = 0
        elementos.pop()
    
    return False


aa = Juego(matriz,Filas, Columnas)
print(aa)
for element in result:
    print(element)