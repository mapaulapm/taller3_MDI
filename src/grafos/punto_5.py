import heapq


def dijkstra(grafo, origen):
    """
    Calcula la distancia mínima desde el nodo origen a todos los demás nodos.

    Parámetros:
        grafo: diccionario de diccionarios
        origen: nodo inicial

    Retorna:
        distancias: distancia mínima desde el origen
        anteriores: nodo anterior en el camino más corto
    """

    # Inicializar distancias
    distancias = {nodo: float("inf") for nodo in grafo}
    distancias[origen] = 0

    # Para reconstruir caminos
    anteriores = {nodo: None for nodo in grafo}

    # Cola de prioridad (distancia, nodo)
    cola = [(0, origen)]

    while cola:
        distancia_actual, actual = heapq.heappop(cola)

        # Si ya encontramos un camino mejor, ignoramos este
        if distancia_actual > distancias[actual]:
            continue

        # Revisar vecinos
        for vecino, peso in grafo[actual].items():
            nueva_distancia = distancia_actual + peso

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = actual
                heapq.heappush(cola, (nueva_distancia, vecino))

    return distancias, anteriores

def reconstruir_camino(anteriores, origen, destino):
    """
    Reconstruye el camino mínimo desde origen hasta destino.
    """

    camino = []
    actual = destino

    while actual is not None:
        camino.append(actual)
        actual = anteriores[actual]

    camino.reverse()

    if camino[0] == origen:
        return camino

    return []

def ingreso_grafo():
    grafo={}

    n=int(input("Ingrese el número de nodos"))
    print("\nIngrese el nombre de cada nodo:")
    for _ in range(n):
        nodo = input("Nodo: ").strip().upper()
        grafo[nodo] = {}

    a = int(input("\nIngrese el número de aristas: "))

    print("\nIngrese las aristas en el formato:")
    print("origen destino peso")

    for i in range(a):
        print(f"\nArista {i+1}:")
        origen, destino, peso = input().split()

        origen = origen.upper()
        destino = destino.upper()
        peso = float(peso)

        grafo[origen][destino] = peso
        grafo[destino][origen] = peso   # Grafo no dirigido

    return grafo   

def eliminar_nodo(grafo, nodo):
    if nodo not in grafo:
        print("El nodo no existe.")
        return

    # Eliminar el nodo
    grafo.pop(nodo)

    # Eliminar las conexiones hacia ese nodo
    for vecino in grafo:
        if nodo in grafo[vecino]:
            del grafo[vecino][nodo]
def eliminar_arista(grafo, origen, destino):
    if destino in grafo[origen]:
        del grafo[origen][destino]

    if origen in grafo[destino]:
        del grafo[destino][origen]

def main():

    print("===== ANÁLISIS DE RED DE TRANSPORTE =====\n")

    # Leer el grafo
    grafo = ingreso_grafo()

    print("\n¿Qué desea cerrar?")
    print("1. Una estación (nodo)")
    print("2. Una conexión (arista)")
    print("3. No cerrar nada")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":

        nodo = input("Ingrese la estación a cerrar: ").upper()

        if nodo not in grafo:
            print("La estación no existe.")
            return

        eliminar_nodo(grafo, nodo)

    elif opcion == "2":

        origen = input("Origen de la conexión: ").upper()
        destino = input("Destino de la conexión: ").upper()

        if origen not in grafo or destino not in grafo:
            print("Algún nodo no existe.")
            return

        eliminar_arista(grafo, origen, destino)

    elif opcion != "3":
        print("Opción inválida.")
        return

    origen = input("\nIngrese el nodo origen: ").upper()

    if origen not in grafo:
        print("El nodo origen no existe.")
        return

    distancias, anteriores = dijkstra(grafo, origen)

    print("\n DISTANCIAS MÍNIMAS ")

    for nodo in sorted(grafo.keys()):
        distancia = distancias[nodo]

        if distancia == float("inf"):
            print(f"{origen} -> {nodo}: No existe camino")
        else:
            print(f"{origen} -> {nodo}: {distancia}")

    print("\n CAMINOS ")

    for nodo in sorted(grafo.keys()):

        camino = reconstruir_camino(anteriores, origen, nodo)

        if camino:
            print(f"{origen} -> {nodo}: {' -> '.join(camino)}")
        else:
            print(f"{origen} -> {nodo}: No existe camino")


if __name__ == "__main__":
    main()       