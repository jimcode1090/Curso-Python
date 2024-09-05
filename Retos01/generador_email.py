# Generador de email en python

print("*** Sistema de generador de email ***")
first_name = input("Ingresa tu nombre: ")
last_name = input("Ingresa tu apellido: ")

email = f'{first_name.lower()}.{last_name.lower()}@utopians.com'

print(f'''Tu email generado por el sistema es: 
        {email}
        *** Felicidades ***
''')


