## Tuplas ##
#Una tupla es un conjunto de elementos con elementos cosntantes, una tupla es inmutable

#Definiendo una tupla, estas son las dos formas de definirlo
my_tuple = tuple()
my_other_tuple = (35, 60 , 30)

my_tuple = (35, 1.64, "Javier", "Go")
print(my_tuple)
print(type(my_tuple)) #Vemos que el sistema ya lo identifica como una tupla

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Javier")) #Cuenta cuantas veces existe el valor en la tupla
print(my_tuple.index("Javier")) #Nos indica la posición del elemento buscado

#my_tuple[1] = 1.80 No se pueden editar los valores de la tupla

#Guardamos ambas tuplas en una nueva variable
my_sum_tuple = (my_tuple + my_other_tuple) #Las tuplas se pueden concatenar
print(my_sum_tuple)

print(my_sum_tuple[3:6]) #Obtenemos los elementos dentro de las posiciones seleccionadas

my_tuple = list(my_tuple) #Cambiamos de tupla a lista, para poder modificar
print(type(my_tuple))

my_tuple[3] = "GoGo"
my_tuple.insert(1, "Azul")
print(tuple(my_tuple))