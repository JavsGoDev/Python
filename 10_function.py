### Functions ###

def my_function():
    print("Esto es una función")

my_function()

#def sum_two_values (first_number: int, second_number: int): Se podría tipar el dato pero al meter texto lo ignorara
def sum_two_values (first_number, second_number):
    print(first_number + second_number)

sum_two_values(5,7)
sum_two_values("5","7")
sum_two_values(5.3,7.6)

def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return 

my_result = sum_two_values_with_return(10,5) #Declaramos una variable para obetener el resultado de la sunción
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}") #Con f accedemos a los valores

print_name("Javier","Go")
print_name(surname="Javier",name="Go") #Se puede asignar directamente el valor intercambiando el orden

def print_name_with_default (name, surname, alias = "sin alias"): #Al poner el valor default ya no es necesario capturarlo
    print(f"{name} {surname} {alias}")

print_name_with_default("paco","javier")
print_name_with_default("paco","javier","Go")

def print_texts(*texts): #Al poner un * podemos poner un número de parametro dinamico
    for text in texts:
        print(text)

print_texts("Hola","python")