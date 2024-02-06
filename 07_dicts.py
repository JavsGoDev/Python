## Diccionarios ##

#Tipos de datos donde podemos guardar clave-Valor, facilidad de acceder a un elemento

#Declarando el diccionario
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Javier","Apellido":"Go","Edad":33, 1:"Python"}  #Pares clave valor

my_dict = {
           "Nombre":"Javier",
           "Apellido":"Go",
           "Edad":33, 
           "Lenguajes":{"Python","Swift","Kotlin"},
           1:"1.64"
           }

print(my_dict)
print(my_other_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro" #Actualizamos el valor de la clave seleccionada
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Don GU" #Agregar un nuevo campo al diccionario
print(my_dict)

del my_dict["Calle"] #Eliminar un solo elemento de nuestro diccionario
print(my_dict)

print("Javier" in my_dict) #Hacemos la busqueda por clave, si ponemos el valor no lo encontrara y pondrá false

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_other_dict.fromkeys(("Nombre",1)))

my_list = ["Nombre",1,"Piso"]

my_new_dict = dict.fromkeys((my_list)) #Nuevo diccionario sin datos

my_new_dict = dict.fromkeys(("Nombre",1,"Piso")) #Nuevo diccionario sin datos
print(my_new_dict)

my_new_dict = dict.fromkeys((my_dict)) #Nuevo diccionario sin datos a partir de un diccionario ya creado
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict) #Nuevo diccionario sin datos a partir de un diccionario ya creado
print(my_new_dict)

#Si deseamos agregar un elemento al diccionario tenemos que cambiar el diccionario a lista para poder sumar el elemento y ahora si crear un nuevo diccionario

my_values = my_new_dict.values()
print(type(my_values))