import random
import time

A = [random.randint(0, 10) for _ in range(9)]
A1 = A[:]
A2 = A[:]
A3 = A[:]

# Función para particionar la lista A3[p..r] en dos sublistas y devolver el índice del pivote
def Partir(A1, p, r):
    x = A1[r]  # Tomar el último elemento como pivote
    i = p - 1  # Índice del elemento más pequeño

    # Recorrer los elementos de p a r-1
    for j in range(p, r):
        if A1[j] <= x:
            i += 1  # Incrementar el índice del elemento más pequeño
            A1[i], A1[j] = A1[j], A1[i]  # Intercambiar A3[i] y A3[j]

    A1[i + 1], A1[r] = A1[r], A1[i + 1]  # Intercambiar el pivote con A3[i+1]
    return i + 1  # Devolver la posición del pivote

# Función principal de QuickSort
def QuickSort(A1, p, r):
    if p < r:
        x = Partir(A1, p, r)  # Obtener el índice del pivote
        QuickSort(A1, p, x - 1)  # Ordenar la sublista antes del pivote
        QuickSort(A1, x + 1, r)  # Ordenar la sublista después del pivot

print("\nLista original:", A1)
ini1 = time.time()
QuickSort(A1, 0, len(A1) - 1)  # Llamar a QuickSort para ordenar la lista
fin1 = time.time()
tiempo1 = fin1 - ini1
print("\nLista ordenada por QuickSort:", A1)
print("\nTiempo de ejecucion: {:.10f}".format(tiempo1))

#EMPIEZA QUICKSORT RANDOM
# Función para particionar la lista A3[p..r] en dos sublistas y devolver el índice del pivote
def Partir(A2, p, r):
    x = A2[r]  # Tomar un elemento aleatorio como pivote (en este caso, el último elemento)
    i = p - 1  # Índice del elemento más pequeño

    # Recorrer los elementos de p a r-1
    for j in range(p, r):
        if A2[j] <= x:
            i += 1  # Incrementar el índice del elemento más pequeño
            A2[i], A2[j] = A2[j], A2[i]  # Intercambiar A3[i] y A3[j]

    A2[i + 1], A2[r] = A2[r], A2[i + 1]  # Intercambiar el pivote con A3[i+1]
    return i + 1  # Devolver la posición del pivote

# Función principal de Randomized Quicksort
def RandomizedQuickSort(A2, p, r):
    if p < r:
        # Elegir un índice aleatorio como pivote y cambiarlo con el último elemento
        random_index = random.randint(p, r)
        A2[random_index], A2[r] = A2[r], A2[random_index]

        x = Partir(A2, p, r)  # Obtener el índice del pivote
        RandomizedQuickSort(A2, p, x - 1)  # Ordenar la sublista antes del pivote
        RandomizedQuickSort(A2, x + 1, r)  # Ordenar la sublista después del pivot

print("\nLista original:", A2)
ini2 = time.time()
RandomizedQuickSort(A2, 0, len(A2) - 1)  # Llamar a QuickSort para ordenar la lista
fin2 = time.time()
tiempo2 = fin2 - ini2
print("\nLista ordenada por RandomQuickSort:", A2)
print("\nTiempo de ejecucion: {:.10f}".format(tiempo2))

#EMPIEZA HEAPSORT
# Función para ordenar una lista utilizando el algoritmo Heapsort
def OrdenHeapSort(A3):
    # Construir un montículo máximo inicialmente
    ConstruirMax(A3)
    size = len(A3)
    # Iterar a través de la lista desde el final hacia el principio
    for i in range(size - 1, 0, -1):
        # Intercambiar el elemento máximo (en la raíz) con el último elemento no ordenado
        A3[0], A3[i] = A3[i], A3[0]
        size = size - 1
        # Llamar a la función MaxHeap para mantener la propiedad de montículo máximo
        MaxHeap(A3, 0, size)

# Función para mantener la propiedad de montículo máximo
def MaxHeap(A3, i, size):
    L = 2 * i + 1
    R = 2 * i + 2
    max = i

    # Comprobar si el hijo izquierdo existe y es mayor que el nodo actual
    if L < size and A3[L] > A3[i]:
        max = L

    # Comprobar si el hijo derecho existe y es mayor que el nodo máximo actual
    if R < size and A3[R] > A3[max]:
        max = R

    # Si el nodo actual no es el máximo, intercambiarlo con el máximo
    if max != i:
        A3[i], A3[max] = A3[max], A3[i]
        # Llamar recursivamente a MaxHeap para mantener la propiedad de montículo máximo en el subárbol
        MaxHeap(A3, max, size)

# Función para construir un montículo máximo inicialmente
def ConstruirMax(A3):
    size = len(A3)
    n = size
    # Comenzar desde el último nodo que tiene hijos
    for i in range(n // 2 - 1, -1, -1):
        # Llamar a la función MaxHeap para mantener la propiedad de montículo máximo
        MaxHeap(A3, i, size)

print("\nLista original:", A3)
ini3 = time.time()
OrdenHeapSort(A3)
fin3 = time.time()
tiempo3 = fin3 - ini3
print("\nLista ordenada por HeapSort:", A3)
print("\nTiempo de ejecucion: {:.10f}".format(tiempo3))