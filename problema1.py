#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)

# Leer las dos listas de entrada y convertir los valores a enteros
# Leer las dos listas de entrada y convertir los valores a enteros


lista1 = tuple(int(x) if x.isdigit() else x for x in input().split())
lista2 = tuple(int(x) if x.isdigit() else x for x in input().split())

nueva_lista = lista2 + lista1 + lista2

print(nueva_lista)
