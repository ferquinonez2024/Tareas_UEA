#tarea semana 15
# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "Tiffany Fernanda Quiñonez Quintero",
    "edad": 19,
    "ciudad": "Esmeraldas",
    "profesion": "ESTUDIANTE UNIVERSITARIA"
}

# Acceder y modificar el valor asociado con la clave "ciudad"
informacion_personal["ciudad"] = "Esmeraldas"

# Agregar una nueva clave-valor para representar la profesión
informacion_personal["profesion"] = "ESTUDIANTE UNIVERSITARIA"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0968778340"

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print("Diccionario de información personal después de las modificaciones:")
print(informacion_personal)
