from tablero import Tablero
from jugador import Jugador
from intento import Intento


def cargar_tableros(ruta_archivo):
    """Lee sudokus.lfp (id_sudoku,dificultad,tablero) y devuelve una lista de Tablero."""
    lista_tableros = []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for numero_linea, linea in enumerate(archivo, start=1):
                linea = linea.strip()
                if not linea:
                    continue
                try:
                    partes = linea.split(',')
                    id_sudoku = int(partes[0])
                    dificultad = partes[1]
                    cadena = partes[2]

                    nuevo_tablero = Tablero(id_sudoku, dificultad, cadena)
                    lista_tableros.append(nuevo_tablero)
                except (IndexError, ValueError) as e:
                    print(f"[!] Línea {numero_linea} de {ruta_archivo} con formato incorrecto, se omite: {e}")
        print(f"[OK] Se cargaron {len(lista_tableros)} tableros con éxito.")
    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo: {ruta_archivo}")
    except Exception as e:
        print(f"[ERROR] No se pudo leer el archivo de tableros: {e}")
    return lista_tableros


def cargar_jugadores(ruta_archivo):
    """Lee jugadores.lfp (carnet,nombre,apellido,nivel) y devuelve una lista de Jugador."""
    lista_jugadores = []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for numero_linea, linea in enumerate(archivo, start=1):
                linea = linea.strip()
                if not linea:
                    continue
                try:
                    partes = linea.split(',')
                    carnet = partes[0]
                    nombre = partes[1]
                    apellido = partes[2]
                    nivel = partes[3]

                    nuevo_jugador = Jugador(carnet, nombre, apellido, nivel)
                    lista_jugadores.append(nuevo_jugador)
                except IndexError as e:
                    print(f"[!] Línea {numero_linea} de {ruta_archivo} con formato incorrecto, se omite: {e}")
        print(f"[OK] Se cargaron {len(lista_jugadores)} jugadores con éxito.")
    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo: {ruta_archivo}")
    except Exception as e:
        print(f"[ERROR] No se pudo leer el archivo de jugadores: {e}")
    return lista_jugadores


def cargar_intentos(ruta_archivo):
    """Lee intentos.lfp (carnet,id_sudoku,solucion,tiempo_segundos,fecha) y devuelve una lista de Intento."""
    lista_intentos = []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for numero_linea, linea in enumerate(archivo, start=1):
                linea = linea.strip()
                if not linea:
                    continue
                try:
                    partes = linea.split(',')
                    carnet = partes[0]
                    id_sudoku = int(partes[1])
                    solucion = partes[2]
                    tiempo_segundos = int(partes[3])
                    fecha = partes[4]

                    nuevo_intento = Intento(carnet, id_sudoku, solucion, tiempo_segundos, fecha)
                    lista_intentos.append(nuevo_intento)
                except (IndexError, ValueError) as e:
                    print(f"[!] Línea {numero_linea} de {ruta_archivo} con formato incorrecto, se omite: {e}")
        print(f"[OK] Se cargaron {len(lista_intentos)} intentos con éxito.")
    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo: {ruta_archivo}")
    except Exception as e:
        print(f"[ERROR] No se pudo leer el archivo de intentos: {e}")
    return lista_intentos
