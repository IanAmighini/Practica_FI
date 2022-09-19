#Practica POO Parte 1

#1
class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2

#La interfaz son los metodos que entiende la clase (energia, comer, acariciar, estaDebil) y el estado son los atributos (alimento y caricias)

#2
class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    if (self.energia > 10 + kms):
        self.energia -= 10 + kms
    else:
        print("No tiene la suficiente energia")

#3
class Notebook:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def descuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)
    
    def precio_actual(self):
        print(self.precio)

notebook1 = Notebook('Asus', 'R556L', 80000)
notebook1.precio_actual()
notebook1.descuento(50)
notebook1.precio_actual()

#4 #5
class Contador:
    def __init__(self, valor):
        self.valor = valor
        self.ultimo = ''
    
    def inc(self):
        self.valor += 1
        self.ultimo = 'incremento'
    
    def dis(self):
        self.valor -= 1
        self.ultimo = 'disminucion'
    
    def reset(self):
        self.valor = 0
        self.ultimo = 'reset'
    
    def valorActual(self):
        print(self.valor)
        self.ultimo = 'valor actual'
    
    def valorNuevo(self, num):
        self.valor = num
        self.ultimo = 'valor nuevo'
    
    def ultimoComando(self):
        print(self.ultimo)

contador = Contador(10)
contador.inc()
contador.inc()
contador.dis()
contador.inc()
contador.valorActual()
contador.valorNuevo(27)
contador.dis()
contador.dis()
contador.valorActual()
contador.ultimo()

#6
class Calculadora:
    def __init__(self):
        self.valor = None
    
    def cargar(self, num):
        self.valor = num
    
    def sumar(self, num):
        self.valor += num
    
    def restar(self, num):
        self.valor -= num
    
    def multiplicar(self, num):
        self.valor *= num

    def valorActual(self):
        print(self.valor)

calculadora = Calculadora()
calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
calculadora.valorActual()

#7
class Gorrion:
    def __init__(self):
        self.gramosActuales = 0
        self.kmsActuales = 0
        self.listaGramos = []
        self.listaKms = []

    def comer(self, gramos):
        self.gramosActuales += gramos
        self.listaGramos.append(gramos)
    
    def volar(self, kms):
        self.kmsActuales += kms
        self.listaKms.append(kms)

    def css(self):
        if self.gramosActuales > 0:
            return self.kmsActuales / self.gramosActuales
        else:
            return None

    def cssp(self):
        return max(self.listaKms) / max(self.listaGramos)
    
    def cssv(self):
        return len(self.listaKms) / len(self.listaGramos)
    
    def estaEnEquilibrio(self):
        return 0.5 <= self.css() <= 2


#Practica POO Parte 2

#1

#Sus estados son caricias y alimento
#Sus interfaces son todos los metodos que entienden
#Comparten parte de su interfaz
#Para decir que son polimorficas necesitamos una tercer clase que use a las 2

#2
class Golondrina:
    def __init__(self, energia):
        self.energia = energia

    def comer_alpiste(self, gramos):
        self.energia += 4 * gramos

    def volar_en_circulos(self):
        self.volar(0)

    def volar(self, kms):
        self.energia -= 10 + kms

    def estaEnEquilibrio(self):
        return 150 <= self.energia <= 300

#3
class Ornitologo:
    def __init__(self):
        self.aves = []

    def estudiarAve(self, ave):
        self.aves.append(ave)
    
    def avesEnEstudio(self):
        return self.aves
    
    def avesEnEquilibrio(self):
        return [self.aves[i].estaEnEquilibrio() for i in range(len(self.aves))]
    
    def realizarRutinaSobreAves(self):
        [self.aves[i].comer(80) for i in range(len(self.aves))]
        [self.aves[i].volar(70) for i in range(len(self.aves))]
        [self.aves[i].comer(10) for i in range(len(self.aves))]

ornitologo = Ornitologo()
golondrina1 = Golondrina(80)
golondrina2 = Golondrina(75)
gorrion1 = Gorrion()
gorrion2 = Gorrion()

#4
class MedioDeTransporte:
    def __init__(self, combustible):
        self.combustible = combustible
    
    def combustibleActual(self):
        return self.combustible
    
    def entran(self, personas):
        return personas <= self.maxPersonas()
    
    def cargarCombustible(self, cantidad):
        self.combustible += cantidad
    
class Moto(MedioDeTransporte):
    def maxPersonas(self):
        return 2
    
    def recorrer(self, km):
        self.combustible -= km
    
class Auto(MedioDeTransporte):
    def maxPersonas(self):
        return 4

    def recorrer(self, km):
        self.combustible -= km/2
    
auto = Auto(100)
moto = Moto(89)