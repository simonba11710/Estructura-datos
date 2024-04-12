# Creacion de variables
edad = 2 #Numerico
Nombre = "Simon" #Caracter
Activo = True #Booleanos
Promedio = 3.4 #Decimales

#Bloques de codigo
#Finalizan en : --> Son funciones, metodos, clases, estructura de control
#Python pone problema por la tabulacion

def calcular_edad(): #Def es Funcion
    pass

if edad > 18: #if es la condicion(condicional)
    pass

#POO 
#Animal= Clase
#Gato,Perro= Objeto
#4 años Zeus= Atributos
#Comer,Caminar= Metodos o funciones
#Clase es una plantilla
#Crear una platinlla para la fabricacion de un vehiculo, combustible y la marca
#Al crear un vehiculo(ej suzuki, debe solicitar el combustible y la marca)
class Automovil: #Class es para crear la plantilla o clase
    combustible = "" #Atributo 1
    marca = "" #Atributo 2

    #Constructor se incia cuando creo un objeto
    def _init_(self, c ,m) -> None: #c y m son los atributos
        self.combustible = c
        self.marca = m

    def arrancar(self): #Metodos o funciones
        print(f"El vehiculo arranca con gasolina {self.combustible}") #Poner f para que reconozca el atributo
    
    def apagar(self): #Metodos o funciones
        pass          #Sefl es el apuntador

moto = Automovil("Suzuki", "Corriente") #crear objeto
moto.arrancar()