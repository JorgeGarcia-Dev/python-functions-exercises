"""
Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python
tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen
ejercicio.
"""

def longitud_cadena(entrada):
    contador = 0
    for i in entrada:
        contador += 1
    return contador

palabra = input("Ingresa una palabra: ")

print(longitud_cadena(palabra))