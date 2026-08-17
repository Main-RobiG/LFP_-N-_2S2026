class Jugador:
    def __init__(self, carnet, nombre, apellido, nivelDificultad):
        self.carnet = carnet
        self.nombre = nombre
        self.apellido = apellido
        self.nivelDificultad = nivelDificultad

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def mostrar_info(self):
        print(f"Carnet: {self.carnet} | Nombre: {self.obtener_nombre_completo()} | Nivel: {self.nivelDificultad}")