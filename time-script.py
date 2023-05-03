import time

# Guardar el tiempo de inicio
inicio = time.perf_counter()

# Aquí va tu código

# Guardar el tiempo de finalización
fin = time.perf_counter()

# Calcular la duración en segundos
duracion = fin - inicio

# Imprimir la duración en segundos
print("El script se ejecutó en", duracion, "segundos.")
