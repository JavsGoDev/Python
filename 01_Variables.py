#Variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

#Convertir entero a string
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

#Transforma todos los datos por debajo a texto para poder imprimir (concatenación de variables)
print(my_string_variable,my_int_variable,my_bool_variable)

print("Este es el valor de :", my_bool_variable)

# Algunas funciones del sistema

# len cuenta los caracteres de la variable
print(len(my_int_to_str_variable))

#Variables en una sola linea (no recomendable)
name, surname , alias, edad = "Dante","Go","chiquitin",1
print("Mi edad es:",edad,"Mi nombre es:",name,surname,alias)

namer = input("Cual es tu nombre?")
print ("Hola",namer)

#Se puede cambiar el tipo de dato
namer = 34
print(namer)

#Forzamos el tipo (no se puede forzar el tipo)
address: str = "Mi dirección" 
address = 32
print(type(address))

