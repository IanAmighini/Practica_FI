#Intoduccion a Python

#Desafio I
mate = input('LLeno o Vacio?: ')
yerbero = input('LLeno o Vacio?: ')
maceta = 'maceta con cactus del balcón'

if mate == 'Vacio':
    print('Llenar el mate con el yerbero')
elif yerbero == 'Vacio':
    print('Llenar el yerbero con yerba')
else:
    print('Vaciar el mate en la', maceta, 'y volverlo a llenar con yerba')

#Para pensar 🤔: ¿Y cómo te parece que funciona tu teléfono celular 📱?
#Funciona igual, nosotros le damos ordenes (entrar a una app) y el celular sabe que acciones hacer para que se ejecute lo que queremos hacer

#Desafio II
#El prompt en mi caso es >>> que es el promt default de python

#Para pensar 🤔:¿Cuál es el resultado? ¿Qué significa entonces el *?
#El resultado es 15 ya que el * significa por (multiplicacion)

#Para pensar 🤔:¿Cuál es el resultado? ¿Qué significa entonces el /?
#El resultado es 2 ya que el / significa dividido (dividir)

edad_lola = 13
edad_ana = 32
edad_lola == edad_ana
#Para pensar 🤔:¿Cuál es el resultado? ¿Qué tipo de dato es?
#El resultado no es nada (esta mal escrito edad_ana en la teorica), por eso tira error
#Si estuviese bien escrito, el resultado seria falso y seria un booleano

afirmacion = "si"
gran_afirmacion = "SI"
gran_afirmacion == afirmacion
#Para pensar 🤔:¿Qué resultado nos da? ¿Por qué?
#Nos da False ya que no es lo mismo mayuscula que minuscula

#Para pensar 🤔:¿Posición tendrá la letra "C' en el string "Marie Curie"? ¿Por qué?
#Tendria la posicion numero 6, arrancando en 0 y el espacio tambien cuenta

#Para pensar 🤔:¿Qué resultado nos dá el código anterior? ¿Por qué? ¿Qué pasa si removemos el último número (hacemos saludo[0:])?
#Nos devuelve 'Hol', y si ponemos [0:] nos da del princpio hasta el final.

#Desafio III
saludo = "Hola mundo"
len(saludo) #Cuenta la cantidad de caracteres del string
saludo.upper() #Convierte el string a mayuscula
saludo.lower() #Convierte el string a minuscula
saludo.count('o') #Cuenta la cantidad de 'o'
saludo.replace('o','a') #Reemplaza las 'o' por 'a'

#Para pensar 🤔: ¿Se podrán combinar los métodos? Probá hacer saludo.upper().lower() ¿Qué dá? ¿Por qué?
#Si, se pueden combinar. El saludo.upper().lower() hace mayusculas a todo el string y luego lo hace minusculas

#Desafio IV
saludo.replace("mundo", "terricolas")
#Si se puede reemplazar por un string mas largo

#Para pensar 🤔: ¿Si imprimís saludo luego de ejecutar la linea anterior qué obtenés? ¿Cambió el valor de la variable?
#Nos da 'Hola terricolas'. Sigue siendo nu string solo que es mas largo que el anterior.

#Para pensar 🤔: ¿Cómo podrías conocer la longitud de la lista?
#Haciendo len(lista)

lista = [2,5,4]
lista.append('25')
lista.remove('25')
#Para pensar 🤔: Probá la sentencia lista.index('25') ¿Qué resultado obtenes? ¿Para qué sirve index()
#No va a encontrar el numero 25 porque lo agregamos a la lista y despues lo sacamos. El index nos sirve para ver en que posicion se encuentra lo que estamos buscando

#Para pensar 🤔: ¿Cómo harías para obtener todos los valores de un diccionario?
#Usaria list(diccionario.values())

#Desafio VI (no hay V)
def mates_para(personas):
    ml = 30*int(personas)
    if 0 < ml <= 1000:
         print('Se necesita 1 termo')
    elif 1000 < ml <= 2000:
         print('Se necesitan 2 termos')
    elif 2000 < ml <= 3000:
         print('Se necesitan 3 termo')
    elif 3000 < ml <= 4000:
         print('Se necesitan 4 termo')
    else:
        print('Son muchos o es un numero negativo')
mates_para(6)

#Desafio VII
facturas = int(input('Cuantos salen las facturas?: '))
def vaquita(personas):
    print('Cada uno aporta',facturas/personas)
vaquita(5)

#Desafio VIII
def calcular_cantidad_de_agua(personas):
    if personas*30 > 1000:
        print('Vas a necesitar mas de 1 termo')
    else:
        print('Se necesitan', personas*30, 'ml')
calcular_cantidad_de_agua(15)

#Para pensar 🤔: ¿Qué nos imprime el procedimiento de anterior? ¿Qué significa i?
# El procedimiento anterior nos imprime .i significa cada elemento

#Desafio IX
pedido = { "Ana" : "no veggie", "Paul": "veganas", "Luz": "vegetarianas"}
lista_comensales = pedido.keys()

def empanadas_por_gusto(): #(modificar)
    for i in lista_comensales:
        print(pedido[i])