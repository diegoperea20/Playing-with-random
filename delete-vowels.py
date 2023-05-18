def eliminar_vocales(palabra):
    vocales = ['a', 'e', 'i', 'o', 'u']
    palabra_sin_vocales = ""
    palabra_con_vocales = ""
    for letra in palabra:
        if letra.lower() in vocales:
            palabra_con_vocales += letra
        else:
            palabra_sin_vocales += letra
    return palabra_sin_vocales, palabra_con_vocales

# Ejemplo de uso
palabra = "onomatopeya"
sin_vocales, con_vocales = eliminar_vocales(palabra)
print("Palabra sin vocales:", sin_vocales)
print("Vocales eliminadas:", con_vocales)

