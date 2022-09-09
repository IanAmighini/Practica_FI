#Practica Intro a Python 1 resuelta

#1
string = input('Escriba algo: ')
print(len(string))

#2
palabra = input('Escriba una palabra: ')
print(palabra[4:6].upper())

#3
nombre = input('Nombre y apellido: ')
print('Hola', nombre)

#4
nom= input('Escriba nombre: ')
ape = input('Escriba primer apellido: ')
ape2 = input('Escriba segundo apellido: ')
print(nom[0].upper(), ape[0].upper(), ape2[0].upper())

#5
num1 = int(input('numero 1: '))
num2 = int(input('numero 2: '))
num3 = int(input('numero 3: '))
print((num1 + num2 + num3)/3)

#6
tiempo = int(input('Cantidad de minutos: '))
print((tiempo // 60), 'horas y', (tiempo % 60), 'minutos')

#7
sueldo = int(input('Sueldo: '))
venta1 = float(input('Venta1: '))
venta2 = float(input('Venta2: '))
venta3 = float(input('Venta3: '))
venta4 = float(input('Venta4: '))
comision = venta1*0.1 + venta2*0.1 + venta3*0.1 +venta4*0.1
print('La comision es:', comision,'El sueldo total es',comision  + sueldo)

#8
resp1 = int(input('Respuestas correcctas: '))
resp2 = int(input('Respuestas incorrecctas: '))
resp3 = int(input('Respuestas en blanco: '))
total_puntos = (resp1*4) + (resp2*(-1))
print(total_puntos)

#Ejercicio en grupo 1
costo_total = int(input('Valor de la casa: '))
porcentaje_deposito = costo_total / 4
cantidad_ahorrada = 0
g = 4
porcentaje_ahorrado = int(input('Cuanto queres ahorrar: '))
sueldo_anual = int(input('Sueldo: '))
sueldo_mensual = sueldo_anual / 12

ahorro_mensual = sueldo_mensual * (porcentaje_ahorrado / 10)
mes = 0
while porcentaje_deposito > cantidad_ahorrada:
    mes += 1
    cantidad_ahorrada += ahorro_mensual + (cantidad_ahorrada * g / 12)
else:
    print('Tenes que ahorar por', mes, 'meses')