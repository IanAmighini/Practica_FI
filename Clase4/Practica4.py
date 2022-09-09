#Practica Expresiones Regluares

import re

#1
def permitido(string):
    return bool(re.search('[a-zA-Z0-9]', string))
print(permitido('hj2h34svJSJ'))

#2
def todo_permitido(string):
    return not bool(re.search('[^a-zA-Z0-9]', string))
print(todo_permitido('lkj#%234HAN'))

#3
def encontrar_patron(string):
    patron = 'he*'
    if re.search(patron, string) is not None:
        return "Esta el patron"
    else:
        return "No esta el patron"
print(encontrar_patron('kkjsdaheee'))

def encontrar_patron2(string):
    patron = 'he+'
    if re.search(patron, string) is not None:
        return "Esta el patron"
    else:
        return "No esta el patron"
print(encontrar_patron2('kkjshdaeee'))

def encontrar_patron3(string):
    patron = 'he{2,3}'
    if re.search(patron, string) is not None:
        return "Esta el patron"
    else:
        return "No esta el patron"
print(encontrar_patron3('kkjsdaheee'))

#4
def palabras_unidas(string):
    patron = '^[a-zA-Z0-9]+_[a-zA-Z0-9]+$'
    if re.search(patron, string) is not None:
        return 'Esta bien'
    else:
        return 'Esta mal'
print(palabras_unidas('KJsa90_ashj87JN'))

#5
def num_especifico(numero, string):
    if re.match(str(numero), string) is not None:
        return 'Empieza con ese numero'
    else:
        return 'No empieza con ese numero'
print(num_especifico(9,'90asfasjn234'))

#6
def se_encuentra(strings, frase):
    for palabra in strings:
        if re.search(palabra, frase) is not None:
            return 'Esta en la frase'
        else:
            return 'No esta en la frase'