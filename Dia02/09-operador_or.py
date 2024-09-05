print('*** OPERADOR LÓGICO OR ***')
# El operador or, si cualquiera de sus variables es True
# toda la expresión es True

condition1 = False
condition2 = False

resultado = condition1 or condition2
print(f'Resultado {condition1} or {condition2}: {resultado}')

condition1 = False
condition2 = True

resultado = condition1 or condition2
print(f'Resultado {condition1} or {condition2}: {resultado}')

condition1 = True
condition2 = False

resultado = condition1 or condition2
print(f'Resultado {condition1} or {condition2}: {resultado}')

condition1 = True
condition2 = True

resultado = condition1 or condition2
print(f'Resultado {condition1} or {condition2}: {resultado}')

# Ejemplo
vacaciones = False
descanso = False

print(f'\n*** ¿Sergio puede asistir al juego de mateo? ***')
print(f'Vacaciones: {vacaciones}, Descanso: {descanso}')
if vacaciones or descanso:
    print('Sergio puede asistir al juego de mateo')
else:
    print('Sergio no puede asistir al juego de mateo, se encuentra trabajando')

print('*** FIN ***')
