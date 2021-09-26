# from persona import Persona
from futbolista import Futbolista

"""
alvaro_arratia = Persona("Alvaro", 25)
patricia_ramirez = Persona("Patricia", 55)

if type(alvaro_arratia) is Persona:
    print(alvaro_arratia)  # No es necesario invocar al metodo __str__
else:
    print("No es persona")

if type(patricia_ramirez) is Persona:
    print(patricia_ramirez)
else:
    print("No es persona")
"""

futbolista = Futbolista("CHUPETE", 30, "delantero")
print(futbolista)