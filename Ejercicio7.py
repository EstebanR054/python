r=float(input('Ingrese el radio del círculo: '))
pi=float(3.14)
result=pi * r ** 2
medida=input('Ingrese la medida de los valores del círculo (m, dm, cm, mm, etc.): ')
print('El área del círculo es: ' + str(round(result,2)) + str(medida) + '^2.')