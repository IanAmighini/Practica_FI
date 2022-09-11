#Manipulacion de archivos

import os, glob

#Desafío I: Creá un archivo de prueba (bio.txt) en la carpeta destinada a los prácticos de la materia.

#Desafío II: Investigá sobre los métodos os.mkdir() y os.listdir()
#el os.mkdir() se usa para crear un directorio en la carpeta donde estas
#el os.listdir() se usa para que nos de una lista de todos los archivos con el directorio especifico que le asignamos

#Desafío III: Abrí el archivo bio.txt y escribí una mini biografía de presentación.
def biografia(archivo):
    with open(archivo, 'w') as file:
        file.write('Hola esta es mi mini biografia')
biografia('bio.txt')

#Para pensar 🤔:¿Cómo darías formato al texto que estas creando?
#le damos forma usando \n, \s, \t, etc

#Para pensar 🤔:¿Qué diferencias notás? ¿Para qué sirve cada método? ¿Que tipo de dato obtenemos en cada caso? Usá la función type() para explorarlo:
#el read() lee todo el texto caracter por caracter y el readlines() lee todo el texto y lo devuelve como una lista.

#Desafio IV: Descargá el archivo manipulacion_archivos.txt y creá un programa que lea su contenido y lo imprima en pantalla el resultado.
def leer(archivo):
    with open(archivo, 'r') as file:
        print(file.readlines())
leer('manipulacion_archivos.txt')

#Para pensar 🤔: ¿Creés que habrá una forma más práctica de leer archivos estructurados o tabulados?
#seguro pero todavia no lo vimos