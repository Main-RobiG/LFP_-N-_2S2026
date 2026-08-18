def cadena_a_matriz(cadena):
    """Convierte un string de 81 caracteres en una matriz de 9x9 (lista de listas)."""
    matriz = []
    for i in range(9):
        fila = []
        for j in range(9):
            caracter = cadena[i * 9 + j]
            fila.append(int(caracter))
        matriz.append(fila)
    return matriz

def validar_filas(matriz):
    filas_validas = 0
    for fila in matriz:
        # Filtramos los ceros (casillas vacías si las hubiera)
        numeros = [n for n in fila if n != 0]
        # Si no hay repetidos, la cantidad de elementos es igual a los elementos únicos
        if len(numeros) == len(set(numeros)):
            filas_validas += 1
    return filas_validas

def validar_columnas(matriz):
    columnas_validas = 0
    for j in range(9):
        columna = []
        for i in range(9):
            columna.append(matriz[i][j])
        numeros = [n for n in columna if n != 0]
        if len(numeros) == len(set(numeros)):
            columnas_validas += 1
    return columnas_validas

def validar_cajas(matriz):
    cajas_validas = 0
    # Recorremos el inicio de cada bloque 3x3 (filas 0, 3, 6 y columnas 0, 3, 6)
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            caja = []
            for r in range(3):
                for c in range(3):
                    caja.append(matriz[i + r][j + c])
            numeros = [n for n in caja if n != 0]
            if len(numeros) == len(set(numeros)):
                cajas_validas += 1
    return cajas_validas

def validar_respeto_pistas(matriz_solucion, matriz_original):
    """Verifica que el jugador no haya modificado los números base del tablero."""
    for i in range(9):
        for j in range(9):
            pista = matriz_original[i][j]
            if pista != 0:
                if matriz_solucion[i][j] != pista:
                    return False
    return True

def procesar_intento_sudoku(cadena_solucion, cadena_original=None):
    """Calcula las 27 comprobaciones y retorna el porcentaje de validez."""
    matriz_sol = cadena_a_matriz(cadena_solucion)
    
    f_validas = validar_filas(matriz_sol)
    c_validas = validar_columnas(matriz_sol)
    b_validas = validar_cajas(matriz_sol)
    
    total_validas = f_validas + c_validas + b_validas
    porcentaje = (total_validas / 27.0) * 100.0
    
    respeto_pistas = True
    if cadena_original:
        matriz_orig = cadena_a_matriz(cadena_original)
        respeto_pistas = validar_respeto_pistas(matriz_sol, matriz_orig)
        
    es_correcto = (total_validas == 27) and respeto_pistas
    
    return round(porcentaje, 2), es_correcto, matriz_sol