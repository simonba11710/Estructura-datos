#Pila: es una estructura de datos que permite almacenar datos de forma secuencial, pero solo se puede acceder a la parte superior de la pila

#Push: insertar elemento nuevo
#Pop: elimina el elemento
#Top:devuelte el elemento
#isEmpty devuelve el valor booleano que indica si la pila esta vacia
#isFull: devuelve el valor booleano que indica si la pila esta llena
#todo ESTO ES EN LA PARTE SUPERIOR
#nodo= esta compuesto por un Dato y apuntador(es el que me indica cual es el siguiente elemento)

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cima = None
    
    def apilar(self, dato):
        nodo = Nodo(dato)
        if self.cima == None: #pregunta quien esta en la cima
            self.cima = nodo #if es condicion
            return
        nodo.siguiente = self.cima
        self.cima = nodo
    
    def desapilar(self):
        if self.cima == None:
            return None
        dato = self.cima.dato
        self.cima = self.cima.siguiente
        return dato

pila = Pila()
pila.apilar(7)
pila.apilar(6)
pila.apilar(5)
pila.apilar(4)

print(pila.desapilar())
print(pila.desapilar())
print(pila.desapilar())
print("termino desapilando")