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
print(se_encuentra(['hola', 'como', 'andan'], 'buenas como andan todos hola'))

#7
def encontrar(string):
    patron = '\w+\s+'
    resultado = re.search(patron, string)
    print(resultado.group())
encontrar("buenas noches!!233  asdad asd as dasd")

#8
string = str(input("Inserte un string: "))
def devolver_num(string):
    num = re.findall(r'\d+', string)
    print("Los números de", string,"son:",*num)
devolver_num(string)

#9
def entre_guiones(string):
    patron = '[\-][\w]+[\-]'
    return re.findall(patron, string)
print(entre_guiones('hola-sadfs- sfd -fsd-'))

#10
def entre_simbolos(string):
    patron = '[\@|\&][\w]+[\@|\&]'
    resultado = re.findall(patron, string)
    for elem in resultado:
        print(re.search(elem,string).span())
    print(resultado)
entre_simbolos('kjh@asdf@jhk&kjbkj&')

#11
def doble_p(lista):
    for string in lista:
        patron = '[P][\w]+'
        resultado = re.findall(patron, string)
        if len(resultado) == 2:
            print(*resultado)
doble_p(["Práctica Python", "Práctica C++", "Práctica Fortran"])

#12
def reemplazo(texto):
    nuevo_t = re.sub('[\s|\_|\:]','|',texto)
    print(nuevo_t)
reemplazo('kjhasd asdj_ ll')

#13
def reemplazo2(texto):
    nuevo_t = re.sub('[\W]','_',texto)
    print(nuevo_t)
reemplazo2('askjdh!.ajk')

#14
def reemplazo3(texto):
    texto2 = re.sub('[\t|\s]',';',texto)
    print(texto2)
reemplazo3('sadf sadf')

#15
def es_correo(mail):
    validacion_de_correo = re.search("[a-zA-Z0-9_\.\-]+[@][a-z]+[\.][a-z]{2,}",mail)
    if validacion_de_correo is not None:
        print("El e-mail ingresado es válido")
    else:
        print("Intente de nuevo")
es_correo('kjsdhfs@gmail.com')