## Strings ##

my_string = "Mi String"
my_other_string = 'Mi Stringss'

print(len(my_string))
print(len(my_other_string))

print(my_string+ ' ' + my_other_string)

my_new_line_string = "Este es un String \n con salto de linea"
print(my_new_line_string)

my_tab_string = "\t Este es un String con tabuloación"
print(my_tab_string)

my_scape_string = "\tEste es un String \n escapado"
print(my_scape_string)

# Formateo

name = "Javs" 
surname = "Go"
edad = 33

#Agregando las variables de string  
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,edad))
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,edad))                # %s imprime un string %d imprime un número
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(edad))
print(f"Mi nombre es {name} {surname} y mi edad es {edad}")                     # Podemos ver la ubicación de donde vamos colocando los datos

#Desempaquetado de caracteres
language = "python"
a,b,c,d,e,f = language
print(a)
print(e)

#División

language_slice = language [1:3]
print(language_slice)
language_slice = language [1:]
print(language_slice)
language_slice = language [-2]
print(language_slice)
language_slice = language [1:2:4]
print(language_slice)

#Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize()) #Letra en mayuscula
print(language.upper()) # Todo en mayusculas
print(language.count("t")) # Cuenta el número de veces que se repite una letra
print(language.isnumeric()) # Valida si es un número
print(language.lower()) # Todas minusculas
print(language.upper().isupper()) # Comprobar si está en mayucula
print(language.startswith("py"))