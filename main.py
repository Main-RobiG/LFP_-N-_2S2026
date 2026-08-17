from tablero import Tablero
from jugador import Jugador
from intento import Intento
import tablero

# Website: https://fsymbols.com/box-drawing/ para el menu
def main():
    print("┌─────────────────────────────────────────┐")
    print("│       TORNEO DE SUDOKU - NUMERIX        │")
    print("├─────────────────────────────────────────┤")
    print("└─────────────────────────────────────────┘")
    
# Prueba de menu

    tablero = "003020600900305001001806400008102900700000008006708200002609500800203009005010300"
    print("Cantidad de caracteres:", len(tablero))

    solucion = "483921657967345821251876493548132976739564128126798235314269587895213746672415309"
    print("Cantidad de caracteres de solucion:", len(solucion))
    
if __name__ == "__main__":
    main()