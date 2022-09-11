#Expresiones Regulares

import re

#Para pensar 🤔: ¿Qué usos crees que podemos darle a las expresiones regulares? Proponé una aplicación concreta para tu carrera/disciplina.
#las expresiones regulares se pueden usar como filtros. Un uso podria ser para segmentar los archivos .txt de una carpeta

#Para pensar 🤔: Dado el siguiente texto:
texto = 'Esta es la linea uno\npalabra en la linea dos\n'
#¿Cómo crees que darán las siguientes búsquedas?
#expresion regular a: '^palabra': va a encontrar un resultado
#expresion regular b: '\Apalabra': no va a encontrar nada
#expresion regular c: 'palabra$': no va a encontrar nada
#expresion regular d: 'palabra\Z': no va a encontrar nada

#Para pensar 🤔: ¿Qué significará la expresión regular "X(.*)Y"? Ennumera algunas de las posibles strings que cumplen con dicha condición.
#la expresion regular significa que busca cero o mas ocurrencias de todo el texto (No se mas)

#Desafío I: ¿Construí la expresión regular que obtenga al menos 4 dígitos?
def cuatro_digitos(string):
    return re.search('[0-9]{4,}', string)
print(cuatro_digitos('nada12345hola'))

#Desafío II: ¿Construí la expresión regular que obtenga al entre 3 y 6 letras minúsculas?
def minusculas(string):
    return re.search('[a-z]{3,6}', string)
print(minusculas('asdasdddddddGGGG'))

#Desafío III: ¿Construí la expresión regular que obtenga todas las apariciones del patrón ab en un string?
def todas(string):
    return re.search('ab*', string)
print(todas('abcdababdfsg'))

#Para pensar 🤔: ¿Existe una única respuesta para los ejercicios? ¿Qué otras alternativas se te ocurren?
#para el desafio I se puede usar \d en vez de [0-9], despues del resto no se otras alternativas

#Desafio IV: ¿Qué expresión regular usarías para extraer el número de estudiantes que hay en una clase según el siguiente texto:
texto2 = 'En la clase de Introducción a la programación hay 30 estudiantes' 
#'\d+'

#Para pensar 🤔: ¿Qué resultado obtenemos al ejecutar en la última linea?
#nos dice que se encontro el patron desde la posicion 22 hasta la 26

#Desafio V: imprimí el fragmento del texto entre la posición 22 y 26 ¿Qué resultado obtenés? ¿Qué quiere decir el mensaje span?
#obtengo la palabra 'amet'. span es las posiciones donde se encuentra el string

#Para pensar 🤔: ¿Qué resultado obtenemos con search()?¿Qué diferencias observan con match()?
#match() encuentra solo al principio del string y search() busca en todo el string

#Para pensar 🤔: ¿Qué resultado obtenemos? ¿Para qué sirve la función group()?
#obtenemos lo que encontro del string. group() nos da los caracteres del patron encontrado.

#Para pensar 🤔: ¿Qué resultado obtenemos?
#nos devuelve en una lista todas las busquedas encontradas

#Desafio VI: Expresá el patron de búsqueda utilizando lo visto anteriormente sobre metacaracteres y rangos.
#no se que pregunta la verdad

#Para pensar 🤔: ¿Qué resultado obtenemos? ¿Para qué sirve la función sub?
#obtenemos el texto pero con el patron cambiado por ###. sub() reemplaza el patron buscado por algo que le decimos nosotros