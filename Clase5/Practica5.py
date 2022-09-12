#Practica Manejo de excepciones

#1
#Si es correcto, pero es impreciso. Se tendria que usar try ... except TypeError.

#2
def dividir(lista1, numero):
    lista2 = []
    for num in lista1:
        try:
            num2 = num/numero
            lista2.append(num2)
        except ZeroDivisionError:
            return "No se puede dividir por cero"
        except TypeError:
            return "No es numero"
        except ValueError:
            return 'Valor incorrecto'
    return lista2
    
print(dividir([2,4,6,8], 'jfg'))

#3
def positivo(lista, numero):
    try:
        if numero > 0:
            lista.append(numero)
        else:
            raise ValueError("El numero es negativo")
    except TypeError:
        "No es numero"

print(positivo([2,4,6,8], 'hola'))