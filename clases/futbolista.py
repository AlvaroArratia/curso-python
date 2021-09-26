from persona import Persona


class Futbolista(Persona):

    posicion: str

    def __init__(self, nombre: str, edad: int, posicion: str):
        super().__init__(nombre, edad)
        self.posicion = posicion

    def set_posicion(self, posicion: str):
        self.posicion = posicion

    def get_posicion(self):
        return self.posicion

    def __str__(self):
        return f"""
        ----Informacion del futbolista----
        Nombre = {self.nombre}
        Edad = {self.edad}
        Posicion = {self.posicion}
        """
