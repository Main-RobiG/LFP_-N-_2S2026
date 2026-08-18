from carga_lfp import cargar_tableros, cargar_jugadores, cargar_intentos
from comprobaciones import cadena_a_matriz, procesar_intento_sudoku
from reportes import (
    generar_reporte_sudokus,
    generar_reporte_jugadores,
    generar_reporte_top10
)

def mostrar_menu():
    print("\n==========================================")
    print("       TORNEO DE SUDOKU - NUMERIX        ")
    print("==========================================")
    print("1. Cargar archivo de sudokus")
    print("2. Cargar archivo de jugadores")
    print("3. Cargar archivo de intentos")
    print("4. Validar y calificar intentos")
    print("5. Generar Reporte: Resumen por Sudoku")
    print("6. Generar Reporte: Rendimiento por Jugador")
    print("7. Generar Reporte: Top 10 Mejores Tiempos")
    print("8. Salir")
    print("==========================================")

def opcion_cargar_sudokus(tableros):
    nuevos = cargar_tableros("archivos/tableros.lfp")
    if nuevos:
        tableros.clear()
        tableros.extend(nuevos)
        for t in tableros:
            t.matriz = cadena_a_matriz(t.cadena_Tablero)
    return tableros

def opcion_cargar_jugadores(jugadores):
    nuevos = cargar_jugadores("archivos/jugadores.lfp")
    if nuevos:
        jugadores.clear()
        jugadores.extend(nuevos)
    return jugadores

def opcion_cargar_intentos(intentos):
    nuevos = cargar_intentos("archivos/intentos.lfp")
    if nuevos:
        intentos.clear()
        intentos.extend(nuevos)
    return intentos

def opcion_validar_intentos(intentos, tableros):
    if not intentos:
        print("\n[!] Primero debe cargar los intentos (Opción 3).")
        return
    if not tableros:
        print("\n[!] Se recomienda cargar los tableros (Opción 1) para validar respeto de pistas.")

    print("\n--- Procesando y Validando Intentos ---")
    for i in intentos:
        # Se cambia id_sudoku por id_Sudoku (con S mayúscula)
        tablero_orig = next((t for t in tableros if str(t.id_Sudoku) == str(i.id_Sudoku)), None)
        cad_orig = tablero_orig.cadena_Tablero if tablero_orig else None
        
        porcentaje, es_correcto, matriz_sol = procesar_intento_sudoku(i.solucion, cad_orig)
        
        i.porcentaje_validez = porcentaje
        i.es_correcto = es_correcto
        i.matriz_solucion = matriz_sol
        
        estado = "CORRECTO (100%)" if es_correcto else f"INCORRECTO ({porcentaje}%)"
        print(f"Carnet: {i.carnet} | Sudoku ID: {i.id_Sudoku} | Estado: {estado}")

def opcion_reporte_1(tableros, intentos):
    if not tableros or not intentos:
        print("\n[!] Debe cargar tableros e intentos antes de generar este reporte.")
        return
    generar_reporte_sudokus(tableros, intentos)

def opcion_reporte_2(jugadores, intentos):
    if not jugadores or not intentos:
        print("\n[!] Debe cargar jugadores e intentos antes de generar este reporte.")
        return
    generar_reporte_jugadores(jugadores, intentos)

def opcion_reporte_3(jugadores, tableros, intentos):
    if not intentos:
        print("\n[!] Debe cargar intentos antes de generar este reporte.")
        return
    generar_reporte_top10(jugadores, tableros, intentos)