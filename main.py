# Referencia de caracteres ASCII y formateo
from menu import (
    mostrar_menu,
    opcion_cargar_sudokus,
    opcion_cargar_jugadores,
    opcion_cargar_intentos,
    opcion_validar_intentos,
    opcion_reporte_1,
    opcion_reporte_2,
    opcion_reporte_3
)

def main():
    tableros = []
    jugadores = []
    intentos = []

    while True:
        mostrar_menu()
        try:
            opcion = int(input("\nSeleccione una opción: "))
        except ValueError:
            print("[!] Por favor ingrese un número válido.")
            continue

        if opcion == 1:
            tableros = opcion_cargar_sudokus(tableros)
        elif opcion == 2:
            jugadores = opcion_cargar_jugadores(jugadores)
        elif opcion == 3:
            intentos = opcion_cargar_intentos(intentos)
        elif opcion == 4:
            opcion_validar_intentos(intentos, tableros)
        elif opcion == 5:
            opcion_reporte_1(tableros, intentos)
        elif opcion == 6:
            opcion_reporte_2(jugadores, intentos)
        elif opcion == 7:
            opcion_reporte_3(jugadores, tableros, intentos)
        elif opcion == 8:
            print("\n¡Gracias por usar LFP Numerix! Saliendo...")
            break
        else:
            print("[!] Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    main()