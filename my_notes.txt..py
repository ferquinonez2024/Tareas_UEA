#tarea_semana16
# Escritura de Archivo de Texto
# Abre el archivo en modo escritura
with open("my_notes.txt", "w") as file:
    # Escribe al menos tres líneas de notas personales en el archivo
    file.write("Nota 1: Este es mi primer recordatorio.\n")
    file.write("Nota 2: Recuerda comprar leche en el supermercado.\n")
    file.write("Nota 3: No olvides enviar el informe antes del viernes.\n")

# Lectura de Archivo de Texto
# Abre el archivo en modo lectura
with open("my_notes.txt", "r") as file:
    # Lee el contenido del archivo línea por línea
    for line in file.readlines():
        # Muestra en la consola cada línea leída
        print(line.strip())


