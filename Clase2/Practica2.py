#Practica Intro a Python 2 resuelta

#1
cadena = input('Cadena: ')
if cadena[0] == cadena[0].lower():
    print('La primer letra es minuscula')
else:
    print('La primer letra es mayuscula')

#2
numero = int(input('Numero: '))
if numero == 0:
    print('El numero es cero y es par')
elif (numero > 0) and (numero % 2 == 0):
    print('El numero es positivo y es par')
elif (numero > 0) and (numero % 2 != 0):
    print('El numero es positivo y es impar')
elif (numero < 0) and (numero % 2 == 0):
    print('El numero es negativo y es par')
else:
    print('El numero es negativo y es impar')

#3
dado = int(input('Numero del dado: '))
if dado > 6 or dado < 1:
    print('Numero incorrecto')
else:
    print(7-dado)

#4
zona = int(input('Zona: '))
peso = int(input('Peso en gramos: '))
if peso < 5000:
    if zona == 1:
        print(peso*10)
    elif zona == 2:
        print(peso*15)
    elif zona == 3:
        print(peso*18)
    elif zona == 4:
        print(peso*24)
    elif zona == 5:
        print(peso*30)
    else:
        print('Zona no valida')
else:
    print('Peso maximo superado')

#5
num_dia = int(input('Numero del dia: '))
if num_dia == 1:
    print('Lunes')
elif num_dia == 2:
    print('Martes')
elif num_dia == 3:
    print('Miercoles')
elif num_dia == 4:
    print('Jueves')
elif num_dia == 5:
    print('Viernes')
elif num_dia == 6:
    print('Sabado')
elif num_dia == 7:
    print('Domingo')
else:
    print('Numero incorrecto')

#6
lista1 = []
for indice in range(5):
    lista1.append(input('Cadena para lista 1: '))
lista1.reverse()
print(lista1)

#7 (No esta bien)
lista_num = []
num = int(input('Ingrese un numero: '))
if num >= 0:
    lista_num.append(num)
    num
else:
    print(lista_num)

#8
listaN1 = []
listaN2 = []
listaN3 = []

for indice in range(5):
    listaN1.append(int(input('Numero para lista 1: ')))
for indice in range(5):
    listaN2.append(int(input('Numero para lista 2: ')))
for indice in range(5):
    listaN3.append(listaN1[indice] + listaN2[indice])
print(listaN3)

#9
