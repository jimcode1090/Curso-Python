print('*** OPERADORES DE ASIGNACIÓN COMPUESTOS ***')
a, b = 10, 15

print(f'Valor inicial de a: {a}')
print(f'Valor inicial de b: {b}')

a += b
print(f'Asignación compuesta - suma (a += b): {a}')

a = 10
a -= b
print(f'Asignación compuesta - resta (a -= b): {a}')

a = 10
a *= b
print(f'Asignación compuesta - multiplicación (a *= b): {a}')

a = 10
a /= b
print(f'Asignación compuesta - división (a /= b): {a}')