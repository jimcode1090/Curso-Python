print('*** REVISION DE VALOR POSITIVO ***')

number = int(input('Qué numero quieres evaluar?: '))

if number > 0:
    print(f'El numero {number} es positivo')
elif number == 0:
    print(f'El numero {number} es cero')
else:
    print(f'El numero {number} no es positivo')