from carga_lfp import cargar_tableros, cargar_jugadores, cargar_intentos
from comprobaciones import cadena_a_matriz, procesar_intento_sudoku

def mostrar_menu():
    print("\n┌─────────────────────────────────────────┐")
    print("│       TORNEO DE SUDOKU - NUMERIX        │")
    print("├─────────────────────────────────────────┤")
    print("│  1. Cargar Archivos (.lfp)              │")
    print("│  2. Procesar Tableros                   │")
    print("│  3. Procesar Intentos                   │")
    print("│  4. Generar Reportes                    │")
    print("│  5. Salir                               │")
    print("└─────────────────────────────────────────┘")

def opcion_cargar_archivos():
    print("\n--- Cargando Archivos LFP ---")
    tableros = cargar_tableros("archivos/tableros.lfp")
    jugadores = cargar_jugadores("archivos/jugadores.lfp")
    intentos = cargar_intentos("archivos/intentos.lfp")
    return tableros, jugadores, intentos

def opcion_procesar_tableros(tableros):
    if not tableros:
        print("\n[!] Primero debe cargar los tableros (Opción 1).")
        return
    
    print("\n--- Procesando y Convirtiendo Tableros a Matriz 9x9 ---")
    for t in tableros:
        t.matriz = cadena_a_matriz(t.cadena_tablero)
        print(f"Tablero ID {t.id_sudoku} ({t.dificultad}) convertido correctamente. Filas: {len(t.matriz)}")

def opcion_procesar_intentos(intentos, tableros):
    if not intentos:
        print("\n[!] Primero debe cargar los intentos (Opción 1).")
        return
    
    print("\n--- Procesando y Validando Intentos ---")
    for i in intentos:
        tablero_orig = None
        for t in tableros:
            if t.id_sudoku == i.id_sudoku:
                tablero_orig = t
                break
        
        cad_orig = tablero_orig.cadena_tablero if tablero_orig else None
        porcentaje, es_correcto, matriz_sol = procesar_intento_sudoku(i.solucion, cad_orig)
        
        i.porcentaje_validez = porcentaje
        i.es_correcto = es_correcto
        i.matriz_solucion = matriz_sol
        
        estado = "RESUELTO CORRECTAMENTE" if es_correcto else "INCORRECTO"
        print(f"Jugador: {i.carnet} | Sudoku: {i.id_sudoku} | Validez: {porcentaje}% | Estado: {estado}")