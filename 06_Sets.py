## Sets ##
# Guarda la información de forma desordenada, trabajo rápido para estructuras no ordenadas, no admite datos repetidos

#Declaradno sets
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inicialmente es un diccionario

my_other_set = {"Javier","Go",33} #Al momento de introducir datos se convierte en set
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("vala")

my_other_set.add("vala") #Un set no admite repetidos

print(my_other_set) #Un set no es una estructura ordenada

print("Go" in my_other_set) #Validamos si un dato existe dentro de un set
print("Ga" in my_other_set) #Validamos si un dato existe dentro de un set

my_other_set.remove("Go") #Eliminasmos información del set
print(my_other_set)

my_other_set.clear()
print(my_other_set)

del my_other_set #Eliminamos el set
#print(my_other_set) name 'my_other_set' is not defined

my_set = {"Javier","Go",33}
my_list = list(my_set)
print(my_list)
print(my_list[0]) #No se recomienda convertir a lista pues se creara con los elementos desorganizados

my_other_set = {"Kotlin","Swift","Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Java"})) #Podemos poner varios union, pero mientras la información siga siendo la misma no la va incluir en el set, a menos que sea diferente información

print(my_new_set.difference(my_set)) #Imprimimos lo que sea diferente a..
