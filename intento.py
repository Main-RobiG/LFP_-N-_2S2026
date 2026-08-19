class Intento:
    """Representa el intento de resolución de un tablero por parte de un jugador."""

    def __init__(self, carnet, id_sudoku, solucion, tiempo_segundos, fecha):
        self.carnet = carnet
        self.id_sudoku = id_sudoku
        self.solucion = solucion
        self.tiempo_segundos = tiempo_segundos
        self.fecha = fecha

        # Resultados que se calculan al validar el intento (Opción 4 del menú)
        self.matriz_solucion = []
        self.porcentaje_validez = 0.0
        self.es_correcto = False

    def mostrar_info(self):
        print(f"Jugador: {self.carnet} | Sudoku ID: {self.id_sudoku} | Tiempo: {self.tiempo_segundos}s")
