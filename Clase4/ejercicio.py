import random

class Nodo:
  """
  Clase que representa un nodo en una lista enlazada.
  """

  def __init__(self, dato):
    self.dato = dato
    self.siguiente = None

def crear_lista_enlazada_recursiva(tamanio):
  """
  Función recursiva que crea una lista enlazada de un tamaño específico.

  Args:
    tamanio: El tamaño deseado para la lista enlazada.

  Returns:
    La referencia al primer nodo de la lista enlazada creada.
  """

  if tamanio == 0:
    return None

  dato_aleatorio = random.randint(1, 100)  # Generar un número aleatorio entre 1 y 100
  nuevo_nodo = Nodo(dato_aleatorio)
  nuevo_nodo.siguiente = crear_lista_enlazada_recursiva(tamanio - 1)
  return nuevo_nodo

def recorrer_lista_enlazada(nodo_inicial):
  """
  Función que recorre una lista enlazada e imprime los datos de cada nodo.

  Args:
    nodo_inicial: La referencia al primer nodo de la lista enlazada.
  """

  if nodo_inicial is None:
    print("La lista enlazada está vacía.")
    return

  nodo_actual = nodo_inicial
  while nodo_actual:
    print(f"Dato: {nodo_actual.dato}")
    nodo_actual = nodo_actual.siguiente

# Ejemplo de uso
tamanio_lista = 5
nodo_cabeza = crear_lista_enlazada_recursiva(tamanio_lista)
recorrer_lista_enlazada(nodo_cabeza)
