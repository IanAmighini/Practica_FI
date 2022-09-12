#Manejo de excepciones

#Desafio I: Descargá y ejecutá el script1_manejo_errores.py

#Para pensar 🤔: ¿Qué tipo de error se obtiene al ejecutar el programa? ¿En dónde se encuentra el error? ¿Cómo te das cuenta?
#tira un SintaxError en la linea 14. El propio error te dice line X (donde se encuentra el error)

#Para pensar 🤔: ¿Qué nos dice el mensaje de excepción? ¿Qué es la excepción de nombre?
#nos dice que el termino divisor no esta definido. La excepcion es omitir algo un una situacion.

#Para pensar 🤔: ¿Qué nos dice el último mensaje de excepción? ¿Qué es la excepción de tipo?
#Nos tira un error de TypeError, es decir que lo que ingresamos esta mal escrito. En este caso dice que no puede sumar un int con un str

#Para pensar 🤔: ¿Qué tipo de excepción se maneja en el código anterior?
#cualquier error lo va a omitir

#Desafio II: Creá una función denominada mitades que tenga como argumento un número e imprima el resultado de la división de ese número por 2
def mitades(num):
    return num / 2
print(mitades(0))

#Para pensar 🤔: ¿Qué crees que ocurrirá cuando ingresas un 9 como parámetro? ¿Y con un 0?
#nada, dividir 9 en 2 da 4.5 y dividir 0 por 2 da 0 

#Desafio III: ¿Cómo mejorarías tu función para que sea capaz de manejar el error de la división por cero? Reescribí la función incorporando una declaración try-except
def mitades(num, num2):
    try: 
        return num / num2
    except ZeroDivisionError:
        return 'No se puede dividir por cero'
print(mitades(3,0))
