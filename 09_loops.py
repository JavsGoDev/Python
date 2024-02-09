### Loops ###

#While 

my_condition = 100

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: #Poner el else es opcional
    print("Mi condición es mayor o igual a 10")

print("La ejecución continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break #Podemos detener el while cuando se llegue a cumplir cierta condición

    print(my_condition)

print("la ejecución continua")

#For

my_list = [35,24,65,52,30,30,17]
           
for element in my_list:
    print(element)

my_tuple = (35, 1.64, "Javier", "Go")

for element in my_tuple:
    print(element)

my_set = {"Javier","Go",33}

for element in my_set:
    print(element)

my_dict = {"Nombre":"Javier","Apellido":"Go","Edad":33, 1:"Python"}

for element in list(my_dict.values()): 
    print(element) #Imprime los elementos no los valores

for element in my_dict:
    print(element)
    if element == "Edad": #Podemos agregar un if dentro del for
        break
    print("Se ejecuta")
else:
    print("El bucle del diccionario a finalizado")

print("La ejecución continua")

for element in my_dict:
    print(element)
    if element == "Edad": #Podemos agregar un if dentro del for
        continue #Continua pero regresando al for nuevamente
    print("Se ejecuta")
else:
    print("El bucle del diccionario a finalizado")