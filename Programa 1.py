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
