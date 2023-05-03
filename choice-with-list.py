import random

#random.seed(43) # for other cases

# Crear una lista con los números del 1 al 6
numeros_dado_list = [1, 2, 3, 4, 5, 6]

# Elegir un número aleatorio de la lista
numero_obtenido = random.choice(numeros_dado_list)

# Imprimir el número obtenido
print("El número obtenido en lista es:", numero_obtenido)

#Conclusion in comparation with choice-range this option in this case is better and fast in ejecution of the code 