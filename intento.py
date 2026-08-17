class Intento:
    def __init__(self, carnet, id_Sudoku, solucion, tiempo_Segundos, dia):
        self.carnet = carnet
        self.id_Sudoku = id_Sudoku
        self.solucion = solucion
        self.tiempo_Segundos = tiempo_Segundos
        self.dia = dia
        
        # Almacenan los resultados de la validación

        self.matriz_solucion = []
        self.porcentaje_validez = 0.0
        self.es_correcto = False

    def mostrar_info(self):
        print(f"Jugador: {self.carnet} | Sudoku ID: {self.id_Sudoku} | Tiempo: {self.tiempo_Segundos}s")