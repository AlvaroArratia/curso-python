# Manejo de excepciones
"""
try:  # Para el control de errores de un codigo susceptible a ellos
    nombre = input("Ingresa tu nombre: ")
    if nombre == "asd":
        nombre_usuario = nombre

    print(nombre_usuario)
except:  # Si es que ocurre un error
    print("Ha ocurrido un error al obtener el nombre.")
else:  # Si es que no ocurre un error
    print("Todo ha funcionado correctamente.")
finally:  # Cuando termina la instruccion completa
    print("Fin del bloque de codigo.")
"""

# Multiples excepciones
"""
try:
    numero = int(input("Ingrese un numero para elevarlo al cuadrado: "))
    print("El cuadrado es: " + str(numero**2))
except TypeError:  # Para mostrar una respuesta al error de tipo TypeError
    print("Debes convertir cadenas de texto a entero.")
except ValueError:  # Para mostrar una respuesta al error de tipo ValueError
    print("Debes ingresar solo numeros.")
except Exception as err:  # Para obtener el error en especifico
    print("Ha ocurrido un error: ", type(err).__name__)  # Para obtener el nombre del tipo de error
else:
    print("Todo ha funcionado correctamente.")
finally:
    print("Fin del bloque de codigo.")
"""

# Excepciones personalizadas o lanzar excepcion
try:
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real.")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completo.")
    else:
        print(f"Bienvenido {nombre}!!")
except ValueError:
    print("Introduce los datos correctamente.")