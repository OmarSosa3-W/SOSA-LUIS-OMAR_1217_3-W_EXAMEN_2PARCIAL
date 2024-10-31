# SOSA-LUIS-OMAR_1217_3-W_EXAMEN_2PARCIAL
Examen del segundo parcial
# PROGRAMA 1:
print() #un linea en blanco al ejecutar

print("SOSA LUIS OMAR 1217_3-W: MI PRIMER PROGRAMA DEL EXAMNEN 2DO PARCIAL") #el nombre del creador 

print() #un linea en blanco al ejecutar
#para definir las varibales o materias que se usaran

asignaturas = ["matematicas", "fisica", "quimica ", "historia", "lengua"]

aprobadas = []

reprobadas = []

#de coloca la condicion para dar indicacion al programa 

for asignatura in asignaturas:

    nota = float(input(f"ingresa la calificacion obtenida {asignatura}: "))
    
    if nota < 6:
    
        reprobadas.append(asignatura)

    if reprobadas:
        
        print("\nDebes recursar las siguienter materias:")
        
        print()
        
        for asignatura in reprobadas:
        
            print(asignatura)
            
            print()
        else:
            
            print(" Después de eso no debes de hacer mas materias")
            
            print()

![image](https://github.com/user-attachments/assets/11470bb6-5e9a-429f-9ee9-58dcf3bbe7c6)
![image](https://github.com/user-attachments/assets/e22f2fbd-b76e-4bd5-b899-8ad6355658db)

# PROGRAMA 2:
print() #un linea en blanco al ejecutar

print("SOSA LUIS OMAR 1217_3-W: MI PRIMER PROGRAMA DEL EXAMNEN 2DO PARCIAL") #el nombre del creador 

print() #un linea en blanco al ejecutar

#aqui es para definir o crear el diccionario que utilizaremos 

asignaturas = {

    "matematicas" : 6,
    
    "fisica" : 4,
    
    "quimica" : 5
}

#se le da la condición que se debe cumplir 

for asignatura, creditos in asignaturas.items():

    print(f"{asignatura} tiene {creditos} creditos")

#para que muestre el total de los creditos
tota
l_creditos = sum(asignaturas.values()print(f"El numero total de creditos de la materia es: {total_creditos}")
print()

![image](https://github.com/user-attachments/assets/161eaeb0-03fd-483b-b08a-aecae1abdc81)
![image](https://github.com/user-attachments/assets/9531805f-cba9-4fb6-a790-c0839f396fcb)

# PROGRAMA 3:
print() #un linea en blanco al ejecutar

print("SOSA LUIS OMAR 1217_3-W: MI PRIMER PROGRAMA DEL EXAMNEN 2DO PARCIAL") #el nombre del creador 

print() #un linea en blanco al ejecutar


#solo se definen las variables en este caso las materias

asignaturas = ["matematicas", "quimica", "historia", "lengua", "fisica"]

#se indica la condicion que se debe cumplir 

for asignatura in asignaturas:

    nota = float(input("ingresa tu nota obtenida en {asignatura}: "))
    
    print(f"en {asignatura} has sacado {nota}")
    
    print() #una linea en blanco al ejecutar


![image](https://github.com/user-attachments/assets/ee5c680b-ce56-4584-ad7f-73cf5287cc79)
![image](https://github.com/user-attachments/assets/d8822250-2021-4f1f-a3fe-4b9df84b3477)

# PROGRAMA 4:
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

![image](https://github.com/user-attachments/assets/af0732b6-6782-4a5a-a1cf-2ee57056ce3d)
![image](https://github.com/user-attachments/assets/9f3f47bd-0684-41ef-ae90-e392c67ae9c0)
