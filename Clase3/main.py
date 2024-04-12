# creaccion de funcion recursiva: es una funcion que se llama asi misma
# crear funcion recursiva con factoriales
# 5! = 5*4*3*2*1 = 120

resultado_factorial = 1     #El resultado factorial se multiplica por i que es el print
for i in range(1,6):
    print(i)
    resultado_factorial = resultado_factorial * i
print(resultado_factorial)

# 5 * 4! - 4 * 3! - 3 * 2! - 2 * 1! - 1 * 0!
# funcion recursiva
def factorial(numero):
    if numero == 1:
        return 1
    return numero * factorial(numero - 1) #else es tambien para una condicion
print(factorial(5))

#Tarea Crear un funcion recursiva que me calcule una multiplicacion a base de sumas
#Tarea Crear un funcion recursiva que calcule una division a base de restas


