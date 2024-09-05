# Generador Id único
from random import randint

print("*** Sistema de generador de Id Unico ***")
first_name = input("Ingresa tu nombre: ")
first_name_2 = first_name[len(first_name) - 2: len(first_name) + 1].upper()

last_name = input("Ingresa tu apellido: ")
last_name_2 = last_name[0:2].upper()


year_birthday = input("Ingresa tu año de nacimiento (YYYY): ")
year_birthday_2 = year_birthday[len(year_birthday) - 2: len(year_birthday) + 1]

# Número aleatorio
randon_number = randint(0, 9999)


print(f'''Hola {first_name} {last_name}.
    Tu Id Unico es: {first_name_2}{last_name_2}{year_birthday_2}{randon_number},
Bienvenido al sistema.
''')
