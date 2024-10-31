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
total_creditos = sum(asignaturas.values())
print(f"El numero total de creditos de la materia es: {total_creditos}")
print()