class Tablero:
    def __init__(self, id_sudoku, dificultad, cadena_tablero):
        self.id_sudoku = id_sudoku
        self.dificultad = dificultad
        self.cadena_tablero = cadena_tablero
        self.matriz = []

    def mostrar_info(self):
        print(f"ID: {self.id_sudoku} | Dificultad: {self.dificultad}")