## listas ## # Arreglos

#Las listas se pueden declarar de estas dos formas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.64, "Javs", "Go"]

print(type(my_other_list))

# Traer el dato en una posición en especifico
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list.count("Javs")) #Busca en la lista cuantas vaces se repite Javs
print(my_list.count(30)) #Busca en la lista cuantas vaces se repite 30

#Nombre de las variables     # Fuente de donde tomo los datos !! Deben de tener el mimso número de elementos p marca error 
age, height, name, surname = my_other_list
print(name)

age, height, name, surname = my_other_list[0],my_other_list[1],my_other_list[2],my_other_list[3]
print(age)

print(my_list + my_other_list)

#Trabajando con los elementos de la lista

#Añadiendo elemento
my_other_list.append("JavsDev") #Con append se va al final de la lista
print(my_other_list)

my_other_list.insert(1,"Rojo") #Elegimos en que posición insertamos el dato
print(my_other_list)

my_other_list[1] = "Azul" #Cambiamos/Actualizamos el valor de un dato especifico de la lista
print(my_other_list)

#Eliminado elementos de la lista
my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30) #Solo elimina el primer 30 pero por que sabemos el dato a eliminar
print(my_list)

my_list.pop() #Elimina el último valor de la lista
print(my_list.pop()) #Muestra el valor eliminado/desapilado
print(my_list)

my_pop_element = my_list.pop(2) #Desapilando el dato en posición 2 y guardandolo en una variable
print(my_pop_element)
#print(my_list.pop(2)) #Muestra el valor eliminado/desapilado en un lugar de la lista en especifico
print(my_list)

del my_list[2] #Hacemos la eliminación del elemento en especifico
print(my_list)

my_new_list = my_list.copy()

my_list.clear() #Borra los elementos de la lista para dejarla vacia
print(my_list)
print(my_new_list)

my_new_list.reverse() #Imprimimos la lista con los valores ordenasdos al reves
print(my_new_list)

my_new_list.sort() #Ordenación de menor a mayor por defecto, aunque se puede especificar en que orden
print(my_new_list)

print(my_new_list[1:2]) #Obtenemos la información dentro de las posiciones que se especifican

# Cambia la vista string
my_list = list("Hola python")
print(my_list)
print(type(my_list))