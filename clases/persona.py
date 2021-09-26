# Definicion clase
class Persona:

    nombre: str
    edad: int

    # Constructor
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    # Getters y setters
    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_edad(self, edad: int):
        self.edad = edad

    def get_edad(self):
        return self.edad

    # Metodo to string
    def __str__(self):
        return f"""
        ----Informacion de la persona----
        Nombre = {self.nombre}
        Edad = {self.edad}
        """
