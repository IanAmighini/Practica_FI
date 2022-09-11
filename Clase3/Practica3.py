#Practica Manipulacion de archivos resuelta

import os, glob

#1
def empieza_con(letra, archivo):
    suma = 0
    with open(archivo, 'r') as file:
        for line in file:
            if (line[0] != letra.lower() or line[0] != letra.upper()):
                suma += 1
    print('Hay', suma, 'archivos que no empiezan con', letra)
empieza_con('p', 'ej1mani.txt')

#2
def leer_lineas(archivo, cant_lineas):
    lineas = open(archivo, 'r').readlines()[:cant_lineas]
    print(*lineas)
leer_lineas('ej1mani.txt', 5)

#3
def leer_ultimas(archivo, cant_lineas):
    lineas = open(archivo, 'r').readlines()[-cant_lineas:]
    print(lineas)
leer_ultimas('ej1mani.txt', 3)

#4
def contar_palabras(archivo):
    file = open(archivo,'r')
    leer = file.read()
    dividir = leer.split()
    print('El archivo tiene', len(dividir), 'palabras')
contar_palabras('ejmani.txt')

#5
def reemplazar(entrada, salida, letra):
    with open(entrada, 'r') as file, open(salida, 'w') as file2:
        for line in file:
            file2.write(line.replace(letra, letra + '\n'))
reemplazar('texto1.txt', 'texto2.txt', 'n')

#6
def sin_saltos(entrada, salida):
    with open(entrada, 'r') as file, open(salida, 'w') as file2:
        for letra in file.read():
            if letra == '\n':
                pass
            else:
                file2.write(letra)
sin_saltos('texto1.txt', 'texto3.txt')

#7
def palabra_larga(archivo):
    file = open(archivo,'r')
    leer = file.read()
    dividir = leer.split()
    larga = ''
    for palabra in dividir:
        if len(palabra) > len(larga):
            larga = palabra
    print('La palabra mas larga es', larga, 'con', len(larga), 'letras')
palabra_larga('ej1mani.txt')

#8
def juntar(archivo1, archivo2, archivo3):
    with open(archivo1, 'r') as file, open(archivo2, 'r') as file2, open(archivo3, 'w') as file3:
        file3.write(file.read())
        file3.write(file2.read())
juntar('texto1.txt','texto2.txt','texto3.txt')        

#9
def frecuencia(archivo):
    with open(archivo, 'r') as file:
        palabras = file.read()
        lista = palabras.split()
        dic = {}
        for palabra in lista:
            dic[palabra] = int(lista.count(palabra)) / int(len(lista))
        print(dic)
frecuencia('ej1mani.txt')

#10
def unir_txt(carpeta1, nombre):
    os.chdir(carpeta1)
    textos = glob.glob('*.txt')
    os.mkdir('Resuelto')
    with open('Resuelto/' + nombre, 'a') as salida:
        for archivo in textos:
            with open(archivo, 'r') as texto:
                salida.write(texto.read() + '\n')
unir_txt('ej10', 'salida.txt')