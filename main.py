# Website: https://fsymbols.com/box-drawing/
# Utilizado para crear bordes y marcos limpios en la consola.

from menu import (
    mostrar_menu,
    opcion_cargar_archivos,
    opcion_procesar_tableros,
    opcion_procesar_intentos
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
            tableros, jugadores, intentos = opcion_cargar_archivos()
        elif opcion == 2:
            opcion_procesar_tableros(tableros)
        elif opcion == 3:
            opcion_procesar_intentos(intentos, tableros)
        elif opcion == 4:
            print("\nOpción 4: Generar Reportes (En desarrollo)")
        elif opcion == 5:
            print("\n¡Gracias por usar Numerix! Saliendo...")
            break
        else:
            print("[!] Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    main()