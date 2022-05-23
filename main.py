from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def eliminar_impares(listax):
    nueva_lista  = filter(lambda x: x % 2, listax)
    return nueva_lista

def sumar_numeros(lista_nueva):
    suma_lista = reduce(lambda x, y: x + y, lista_nueva)
    return suma_lista

print(sumar_numeros(eliminar_impares(lista)))