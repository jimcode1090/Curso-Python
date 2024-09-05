print('*** OPERADOR LÓGICO AND ***')
# El operador and, si cualquiera de sus variables es False
# toda la expresión es False

condition1 = False
condition2 = False

resultado = condition1 and condition2
print(f'Resultado {condition1} and {condition2}: {resultado}')

condition1 = False
condition2 = True

resultado = condition1 and condition2
print(f'Resultado {condition1} and {condition2}: {resultado}')

condition1 = True
condition2 = False

resultado = condition1 and condition2
print(f'Resultado {condition1} and {condition2}: {resultado}')

condition1 = True
condition2 = True

resultado = condition1 and condition2
print(f'Resultado {condition1} and {condition2}: {resultado}')

# Ejemplo
llueve = False
nublado = False

print(f'\n*** REVISIÓN DEL CLIMA ***')
if llueve and nublado:
    print('Hace mucho lluvia y esta nublado')
elif llueve:
    print('Hace lluvia')
elif nublado:
    print('Esta nublado')
else:
    print('No hace lluvia, ni esta nublado')

print('*** FIN ***')