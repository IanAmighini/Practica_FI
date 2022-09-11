#Practica Intro a Python 2 resuelta

#1
from xmlrpc.server import _DispatchArity3


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

#7
lista_num = []
while int(input('Ingrese un numero: ')) >= 0:
    lista_num.append()
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
nombre_edad = {}
print("Nombre y edad de los alumnos. Escriba * para finalizar")
while True:
    nombre_apellido = input("Nombre y apellido: ")
    edad= input("Edad: ")
    if nombre_apellido != "*":
        nombre_edad[nombre_apellido]= edad 
    else:
        break
edad_maxima = 0
for nombre in nombre_edad:
    if int(nombre_edad[nombre_apellido]) > int(edad_maxima):
        edad_maxima = nombre_edad[nombre]
        
print("la edad maxima es de", edad_maxima, "años, y es", nombre )

#10
dic= {}
palabra = input("Cuantos caracteres tiene: ")
for lista in palabra:
    dic[lista]=0
for listas in palabra:
    dic[listas]= dic[listas] + 1 
print(dic)

#12
dic2= {}
print(int(input("Cantidad de alumnos para cargar: ")))
while True:
    print("coloque * para finalizar")
    nombre_appelido= input("Nommbre y apellido del alumno: ")
    if nombre_appelido != "*":
        while True:
            print("Escriba -1 para pasar al siguiente alumno: ")
            nota= int(input("Notas: "))
            if nota >= 0:
                if nombre_appelido not in dic:
                    dic2[nombre_appelido]=[nota]
                else:
                    dic2[nombre_appelido].append(nota)
            else:
                break
    else:
        break
final = {}
for nombre_appelido in dic2:
    final[nombre_appelido]= (sum(dic2[nombre_appelido])/len(dic[nombre_appelido]))
print(final)

#13
def es_multiplo (num1, num2):
    if num1 / num2 == int(num1/num2) or num2 / num1 == int(num2/num1): 
        print("son multiplos")
    else:
        print("no son multiplos")
es_multiplo(2,10)

#14
def tmp_promedio(max, min):
    print("temperatura promedio",(max+min)/2,"grados")

dias = int(input("cantidad de dias: "))
contador = 0
for dia in range(dias):
    if contador < dias:
        maxima = int(input("Temp. max: "))
        minima = int(input("Temp. min: "))
        tmp_promedio(maxima,minima)
        contador =+ 1
print("Espero que te sirva")

#15

dic3={
1:["Florencia Ocampo", "14/09/2001", "si"],

2:["David Estévez", "14/09/2001", "si"],

3:["Sofía Cáceres", "14/09/2001", "si"]
}
while True:
    print("cargar numero de socio, para finalizar colocar 0 ")
    numero_socio= int(input("Numero de socio: "))
    if numero_socio != 0:
        nombre_appelido= input("Nombre y apellido: ")
        fecha= input("Fecha de ingreso: ")
        cuota= input("Cuota al dia si/no: ")
        dic3[numero_socio]=[nombre_appelido,fecha,cuota]
    else:
        break
print("El club tine",len(dic3),"socios")
    
verificar = input("¿Verificar cuotas de socios? si/no: ")
if verificar.upper() == "SI":
    while True:
        print("Introduzca 0 para finalizar")
        socio=int(input("Numero del socio: "))
        if socio != 0:
            if socio not in dic3:
                print("Este socio no existe")
            else: 
                if dic3[socio][-1].upper() == "SI":
                    print("El",dic3[socio][0],"esta al dia")
                else:
                    print("El",dic3[socio][0],"no esta al dia")
                    
        else:
            break
else:
    pass

dic_copy={}

eliminar = input("Eliminar socio si/no: ")
if eliminar.upper() == "SI":
    while True:
        print("Para finalizar coloque 0")
        elim= input("Numero del socio: ")
        if elim != "0":
            for elemento in dic3:
                if elim.upper() != dic3[elemento][0].upper():
                    dic_copy[elemento]=dic3[elemento]
            
            else:
                break       
else:
    pass
dic3 = dic_copy

cambiar = input("Cambiar fecha socios si/no: ")
if cambiar.upper() == "SI":
    while True:
        print("Para terminar, ingresa 0")
        elim = input("fecha a cambiar: ")
        if elim != "0":
            fecha_nueva= input("nueva fecha: ")
            for elemento in dic3:
                if dic3[elemento][1] == elim:
                    dic3[elemento][1]=fecha_nueva
        else:
            break
else:
    pass

print(dic3)