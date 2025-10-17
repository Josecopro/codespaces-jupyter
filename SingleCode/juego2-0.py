def Juego(matriz, ResultadoFilas, ResultadoColumnas, fila=0, col=0, usados=None, suma_filas=None, suma_cols=None):
    n = len(matriz)
    if usados is None:
        usados = set()
        suma_filas = [0]*n
        suma_cols = [0]*n
    
    if fila == n:  # Todas las filas llenas
        return suma_filas == ResultadoFilas and suma_cols == ResultadoColumnas
    
    # Encontrar siguiente celda (MRV → más restringida)
    SiguienteFila, SiguienteCol = fila, col+1
    if SiguienteCol == n:
        SiguienteFila += 1
        SiguienteCol = 0
    
    for valor in range(1, n*n + 1):
        if valor in usados:
            continue
        
        # Verificación de poda inmediata
        if suma_filas[fila] + valor > ResultadoFilas[fila]:
            continue
        if suma_cols[col] + valor > ResultadoColumnas[col]:
            continue
        
        # Verificación de consistencia aritmética
        faltan_celdas_fila = n - (col+1)
        faltan_celdas_col = n - (fila+1)
        max_fila = suma_filas[fila] + valor + (faltan_celdas_fila * (n*n))
        min_fila = suma_filas[fila] + valor + faltan_celdas_fila
        if not (min_fila <= ResultadoFilas[fila] <= max_fila):
            continue
        max_col = suma_cols[col] + valor + (faltan_celdas_col * (n*n))
        min_col = suma_cols[col] + valor + faltan_celdas_col
        if not (min_col <= ResultadoColumnas[col] <= max_col):
            continue
        
        # Asignación
        matriz[fila][col] = valor
        usados.add(valor)
        suma_filas[fila] += valor
        suma_cols[col] += valor
        
        if Juego(matriz, ResultadoFilas, ResultadoColumnas, SiguienteFila, SiguienteCol, usados, suma_filas, suma_cols):
            return True
        
        # Backtrack
        usados.remove(valor)
        suma_filas[fila] -= valor
        suma_cols[col] -= valor
        matriz[fila][col] = 0
    
    return False



# -------------------------
# EJEMPLO DE PRUEBA N = 5
# -------------------------
n = 5
matriz = [[0]*n for _ in range(n)]
Filas = [65]*n
Columnas = [65]*n

if Juego(matriz, Filas, Columnas):
    print("✅ Solución encontrada:")
    for fila in matriz:
        print(fila)
else:
    print("❌ No hay solución")
