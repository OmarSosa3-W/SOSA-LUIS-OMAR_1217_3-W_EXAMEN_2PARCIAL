print()  # Para dejar una línea en blanco al ejecutar
print("SOSA LUIS OMAR 1217 3-W: MI PRACTICA DE DICCIONARIOS Examen 2DO PARCIAL")  # Nombre del creador del código
print()  # Para dejar una línea en blanco al ejecutar

def obtener_datos_usuario():  # Inicio de la función
    usuario = {}
    usuario['nombre'] = input("¿Cuál es tu nombre? ")  # Pide ingresar el nombre
    print()  # Para dejar una línea en blanco al ejecutar
    usuario['edad'] = input("¿Cuántos años tienes? ")  # Pide ingresar la edad
    print()  # Para dejar una línea en blanco al ejecutar
    usuario['direccion'] = input("¿Dónde vives? ")  # Pide ingresar el lugar de vivienda
    print()  # Para dejar una línea en blanco al ejecutar
    usuario['telefono'] = input("¿Cuál es tu número de teléfono? ")  # Pide ingresar el número de teléfono
    print()  # Para dejar una línea en blanco al ejecutar
    return usuario

def mostrar_informacion(usuario):
    # Muestra la información del usuario de forma clara
    print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}.")

usuario = obtener_datos_usuario()  # Obtiene los datos del usuario
mostrar_informacion(usuario)  # Muestra la información del usuario
print()  # Para dejar una línea en blanco al ejecutar

