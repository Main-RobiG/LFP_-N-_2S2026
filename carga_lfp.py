from tablero import Tablero
from jugador import Jugador
from intento import Intento

def cargar_tableros(ruta_archivo):
    lista_tableros = []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    partes = linea.split(',')
                    id_sudoku = int(partes[0])
                    dificultad = partes[1]
                    cadena = partes[2]
                    
                    nuevo_tablero = Tablero(id_sudoku, dificultad, cadena)
                    lista_tableros.append(nuevo_tablero)
        print(f"[OK] Se cargaron {len(lista_tableros)} tableros con éxito.")
    except Exception as e:
        print(f"[ERROR] No se pudo leer el archivo de tableros: {e}")
    return lista_tableros

def cargar_jugadores(ruta_archivo):
    lista_jugadores = []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    partes = linea.split(',')
                    carnet = partes[0]
                    nombre = partes[1]
                    apellido = partes[2]
                    nivel = partes[3]
                    
                    nuevo_jugador = Jugador(carnet, nombre, apellido, nivel)
                    lista_jugadores.append(nuevo_jugador)
        print(f"[OK] Se cargaron {len(lista_jugadores)} jugadores con éxito.")
    except Exception as e:
        print(f"[ERROR] No se pudo leer el archivo de jugadores: {e}")
    return lista_jugadores

def cargar_intentos(ruta_archivo):
    lista_intentos = []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    partes = linea.split(',')
                    carnet = partes[0]
                    id_sudoku = int(partes[1])
                    solucion = partes[2]
                    tiempo = int(partes[3])
                    fecha = partes[4]
                    
                    nuevo_intento = Intento(carnet, id_sudoku, solucion, tiempo, fecha)
                    lista_intentos.append(nuevo_intento)
        print(f"[OK] Se cargaron {len(lista_intentos)} intentos con éxito.")
    except Exception as e:
        print(f"[ERROR] No se pudo leer el archivo de intentos: {e}")
    return lista_intentos