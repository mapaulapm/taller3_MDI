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


def main():

    grafo = {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "C": 1, "D": 5},
        "C": {"A": 2, "B": 1, "D": 8, "E": 10},
        "D": {"B": 5, "C": 8, "E": 2, "F": 6},
        "E": {"C": 10, "D": 2, "F": 3},
        "F": {"D": 6, "E": 3},
    }

    origen = input("Nodo origen: ").upper()

    if origen not in grafo:
        print("El nodo no existe.")
        return

    distancias, anteriores = dijkstra(grafo, origen)

    print("\nDISTANCIAS MÍNIMAS")

    for nodo in grafo:
        print(f"{origen} -> {nodo}: {distancias[nodo]}")

    print("\n CAMINOS ")

    for nodo in grafo:
        camino = reconstruir_camino(anteriores, origen, nodo)
        print(f"{origen} -> {nodo}: {' -> '.join(camino)}")


if __name__ == "__main__":
    main()

