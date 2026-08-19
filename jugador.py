class Jugador:
    """Representa a un jugador inscrito en el torneo."""

    def __init__(self, carnet, nombre, apellido, nivel):
        self.carnet = carnet
        self.nombre = nombre
        self.apellido = apellido
        self.nivel = nivel

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def mostrar_info(self):
        print(f"Carnet: {self.carnet} | Nombre: {self.obtener_nombre_completo()} | Nivel: {self.nivel}")
