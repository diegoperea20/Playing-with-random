import random
lista=[]
while True:
    a =input("QUIERES AGREGAR algo a la lista: si o no:  ")
    if a == "si":
        b=input("ingresa lo que quieres agregar : ")
        lista.append(b)
    else:
        break

print(lista)

while True:
    seleccion = random.choice(lista)
    print(f'la seleccion random es : {seleccion}')
    lista.remove(seleccion)
    print(lista)
    c=input("quieres agregar otra seleccion al azar : si o no: ")
    if c == "si":
        continue
    else:
        break




