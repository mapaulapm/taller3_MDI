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


