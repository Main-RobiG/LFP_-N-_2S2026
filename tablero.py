class Tablero:
    def __init__(self, id_Sudoku, dificultad, cadena_Tablero):
        self.id_Sudoku = id_Sudoku
        self.dificultad = dificultad
        self.cadena_Tablero = cadena_Tablero
        self.matriz = []

    def mostrar_info(self):
        print(f"ID: {self.id_Sudoku} | Dificultad: {self.dificultad}")