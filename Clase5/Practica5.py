#Practica Manejo de excepciones

#1
#Si es correcto, pero es impreciso. Se tendria que usar try ... except TypeError.

#2

def dividir(lista1, numero):
    lista2 = []
    try:
        for indice in lista1:
            lista2.append(lista1[indice]/numero)
        return lista2
    except ZeroDivisionError:
        "No se puede dividir por cero"
    except TypeError:
        "No es numero"
    
print(dividir([2,4,6,8], 2))

#3
