#Practica Manejo de excepciones

#1
#Si es correcto, pero es impreciso. Se tendria que usar try ... except TypeError.

#2 (modificar)
def dividir(lista1, numero):
    lista2 = []
    for num in lista1:
        try:
            lista2.append(lista1[num]/numero)
        except ZeroDivisionError:
            return "No se puede dividir por cero"
        except TypeError:
            return "No es numero"
    return lista2
    
print(dividir([2,4,6,8], 2))

#3
def positivo(lista, numero):
    try:
        if numero > 0:
            lista.append(numero)
            return lista
        else:
            return "El numero es negativo"
    except TypeError:
        return "No es numero"

print(positivo([2,4,6,8], 'hola'))