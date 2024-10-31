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
