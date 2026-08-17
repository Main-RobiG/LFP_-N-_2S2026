from carga_lfp import cargar_tableros, cargar_jugadores, cargar_intentos

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
            print("\n--- Cargando Archivos LFP ---")
            tableros = cargar_tableros("archivos/tableros.lfp")
            jugadores = cargar_jugadores("archivos/jugadores.lfp")
            intentos = cargar_intentos("archivos/intentos.lfp")
        elif opcion == 2:
            print("\nOpción 2: Procesar Tableros (En desarrollo)")
        elif opcion == 3:
            print("\nOpción 3: Procesar Intentos (En desarrollo)")
        elif opcion == 4:
            print("\nOpción 4: Generar Reportes (En desarrollo)")
        elif opcion == 5:
            print("\n¡Gracias por usar Numerix! Saliendo...")
            break
        else:
            print("[!] Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    main()