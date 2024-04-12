#Tarea Crear un funcion recursiva que me calcule una multiplicacion a base de sumas
#Tarea Crear un funcion recursiva que calcule una division a base de restas

#Tarea1
def multiplicacion_recursiva(multiplicando, multiplicador):
  """
  Calcula la multiplicación de dos números enteros usando sumas recursivas.

  Args:
    multiplicando: El numero que se va a multiplicar.
    multiplicador: El número por el que se va a multiplicar el multiplicando.

  Returns:
    El producto del multiplicando y el multiplicador.
  """

  if multiplicador == 0:
    return 0
  else:
    return multiplicando + multiplicacion_recursiva(multiplicando, multiplicador - 1)

# Ejemplo de uso
producto = multiplicacion_recursiva(4, 3)
print(f"El producto de 4 por 3 es: 4 + 4 + 4 = {producto}") 

#Tarea2
def division_recursiva(dividendo, divisor):
  """
  Calcula el cociente y el resto de la división de dos números enteros positivos usando restas recursivas.

  Args:
    dividendo: El número que se va a dividir.
    divisor: El número por el que se va a dividir el dividendo.

  Returns:
    Una tupla que contiene el cociente y el resto de la división.
  """

  if dividendo < divisor:
    return 0, dividendo
  else:
    cociente, resto = division_recursiva(dividendo - divisor, divisor)
    return cociente + 1, resto % divisor

# Ejemplo de uso
cociente, resto = division_recursiva(10, 3)
print(f"El cociente de 10 entre 3 es: {cociente}") 
print(f"El resto de 10 entre 3 es: {resto}") 

